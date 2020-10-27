import os, math, tempfile


def identify_missing_bids(source_list_filename: str, dest_list_filename: str,
                          subject_savename: str = None, missing_savename: str = None) -> (list, list):
    """
    Given a list of files in the source and the destination, this function creates a list of files which still need to
    be transferred. The purpose is to speed up rsync.

    Parameters
    ----------
    source_list_filename : str
        Filename of the list of files to be transferred. (e.g. find BIDS/ -type l > source_list.txt)
    dest_list_filename : str
        Filename of the list of files to be transferred (e.g. find BIDS/ -type f > dest_list.txt)
    subject_savename : str
        Optional. Filename for the subject list.
    missing_savename : str
        Optional. Filename for the complete list of missing files.

    Returns
    ----------
    list
        List of subjects that have missing files.
    list
        List of all missing files.
    """
    # Read full
    f = open(source_list_filename, 'r')
    full_list = f.readlines()
    f.close()
    # Read partial
    f = open(dest_list_filename, 'r')
    partial_list = f.readlines()
    f.close()

    # Parse lists; remove everything before sub-
    i = 0
    sub_ind_full = full_list[i].find('sub-')
    while sub_ind_full == -1:
        sub_ind_full = full_list[i].find('sub-')
        i += 1
    i=0
    sub_ind_part = partial_list[i].find('sub-')
    while sub_ind_part == -1:
        sub_ind_part = partial_list[i].find('sub-')
        i += 1

    for ind, fl in enumerate(full_list):
        full_list[ind] = fl[sub_ind_full:]
    for ind, pt in enumerate(partial_list):
        partial_list[ind] = pt[sub_ind_part:]

    # Generate requires_transfer list

    for pt in partial_list:
        try:
            ind = full_list.index(pt)
            del full_list[ind]
            # Found; don't add subject
        except ValueError:
            # Not found; add subject
            continue
    # Full_list is now requires_transfer list; transfer to sub_list
    sub_list = []
    for fl in full_list:
        sub = fl.split(os.sep)[0]
        if(sub not in sub_list):
            sub_list.append(sub)
    if(subject_savename is not None):
        f = open(subject_savename,'w')
        for s in sub_list[1:]:
            f.write(s + '\n')
        f.close()
    if(missing_savename is not None):
        f = open(missing_savename, 'w')
        for s in full_list:
            f.write(s+'\n')
        f.close()

    return sub_list, full_list


def merge_fetched(fetched_dir: str) -> list:
    """
    Given a directory with multiple .lis files generated by ukbfetch, this function returns a single, merged file.
    Parameters
    ----------
    fetched_dir : str
        Directory name with multiple .lis files

    Returns
    ----------
    list
        List of fetched files.
    """
    dirlist = os.listdir(fetched_dir)
    fetched_all = []
    for fil in dirlist:
        if('.lis' in fil):
            f = open(os.path.join(fetched_dir, fil), 'r')
            fetched_buf = f.readlines()
            f.close()
            for fetched in fetched_buf:
                fetched_all.append(fetched.split('.')[0])
    return fetched_all


def reduce_bulk_from_fetched(bulk_filename: str, fetched_filename: str, save_file: str=None) -> list:
    """
    Reduces a raw bulk file to a bulk file containing only data which has not been downloaded.

    Parameters
    ----------
    bulk_filename : str
        Filename for the ukbb.bulk file
    fetched_filename : str
        Filename for the list of fetched files (either .lis, or saved from merge_fetched())
    save_file : str
        Optional. Filename to save the list of missing files.

    Returns
    ----------
    list
        List of missing files.
    """
    # Open bulk
    f = open(bulk_filename,'r')
    bulk_list = f.readlines()
    f.close()
    # Open fetched
    f = open(fetched_filename,'r')
    fetched_list = f.readlines()
    f.close()
    # Clean fetched in case .zip is present
    for ind, fetched in enumerate(fetched_list):
        if('.zip' in fetched):
            buf = fetched.split('.zip')[0]
            # Split into [subject] [datafield] pairs
            sub_split = buf.split('_')
            fetched_list[ind] = '{} {}\n'.format(sub_split[0], '_'.join(sub_split[1:]))

    missing_list = []
    # Iterate through bulk; if not in fetched, add to missing
    for bulked in bulk_list:
        if(bulked not in fetched_list):
            missing_list.append(bulked)
    # If save file is specified, save missing list
    if(save_file is not None):
        # save missing_list
        f = open(save_file,'w')
        for mis in missing_list:
            if(mis[-1] != '\n'):
                f.write(mis + '\n')
            else:
                f.write(mis)
        f.close()

    return missing_list


def generate_bulk_slurm(bulk_filename: str, key_filename: str, save_name: str, ukbfetch_loc: str,
                        download_dir: str = './', field: str=None, num_jobs: int = 10, connection_speed: int = 10,
                        slurm_account: str = None, average_file_size: int = 500,
                        ukbfetch_max_files: int = 1000) -> None:
    """
    Generates a SLURM job file to match program constraints. UKBB allows up to 10 simultaneous downloads, and the
    ukbfetch utility allows up to 1000 lines per call.

    Parameters
    ----------
    bulk_filename : str
        Filename of the .bulk file listing the data to be fetched.
    key_filename : str
        Filename for the key file associated with the bulk file.
    save_name : str
        Filename for the SLURM file
    ukbfetch_loc : str
        Filepath for ukbfetch utility
    download_dir : str
        Optional. Path where to download data.
    num_jobs : int
        Optional. Number of jobs across which to split the downloads (i.e. number of simultaenous downloads). WARNING: values
        greater than 10 are likely to cause problems. Default: 10
    connection_speed : float
        Optional. Approximate value in MB/s of transfer speed. Used for requesting resource time from SLURM.
    slurm_account : str
        Optional. Specify the name of the account to use for accounting purposes.
    average_file_size : int
        Optional. Average incoming file size in MB.
    ukbfetch_max_files : int
        Optional. Maximum number of files per bulk file.
    Returns
    ----------
    None
    """
    # Max number of simultaneous downloads is 10
    # (https://biobank.ndph.ox.ac.uk/showcase/docs/ukbfetch_instruct.html, section 2)
    # ukbfetch can fetch up to 1,000 lines (docs say 50k; program says 1k)

    f = open(save_name, 'w')
    if(num_jobs>10):
        Warning('num_jobs greater than 10 is likely to cause download failures (requested {})'.format(num_jobs))
    f.write('#!/bin/bash\n')
    if(slurm_account is not None):
        f.write('#SBATCH --account ' + slurm_account + '\n')
    f.write('#SBATCH --array=0-' + str(num_jobs-1) + '\n')
    f.write('#SBATCH --mem-per-cpu=4096M\n')  # 2GB occasionally causes SLURM to kill the job

    # Count number of files
    bulk_file = open(bulk_filename, 'r')
    bulk_list = bulk_file.readlines()
    bulk_file.close()

    # If 'field' is defined; restrict bulkfile count to only field
    if(field is not None):
        num_files = sum([field in b for b in bulk_list])
    else:
        num_files = len(bulk_list)
    num_files_per_job = math.ceil(num_files / num_jobs)
    expected_time_per_job = num_files_per_job * average_file_size / connection_speed * 1.2  # 20% margin of error

    expected_time = _convert_seconds(expected_time_per_job)
    f.write('#SBATCH --time={}-{}:{}\n\n'.format(*expected_time))

    localscratch = '${SLURM_TMPDIR}'
    # Copy ukbfetch, key and bulk file to local scratch (frequent access, doesn't need to be transferred back)
    f.write(f'cp {ukbfetch_loc} {localscratch}/ukbfetch\n')
    f.write(f'chmod u+x {localscratch}/ukbfetch\n')
    f.write(f'cp {key_filename} {localscratch}/keyfile\n')
    if(field is not None):
        f.write(f'grep {field} {bulk_filename}' + ' >> ${SLURM_TMPDIR}/bulkfile.bulk\n')
    else:
        f.write(f'cp {bulk_filename} {download_dir}/bulkfile.bulk\n')
    # f.write(f'export {localscratch}\n\n')
    f.write(f'cd {download_dir}\n\n')

    bulk_opt = '${SLURM_TMPDIR}/bulkfile.bulk'
    key_opt = '${SLURM_TMPDIR}/keyfile'
    fetched_opt = 'fetched_$((SLURM_ARRAY_TASK_ID))_{fetch_ind}'
    start_opt = '$((SLURM_ARRAY_TASK_ID*' + str(num_files_per_job) + '+{0}))'
    num_opt='{0}'



    # fetch_string = './ukbfetch -b${SLURM_TMPDIR}/bulkfile.bulk -a${SLURM_TMPDIR}/keyfile ' \
    #                '-ofetched_$((SLURM_ARRAY_TASK_ID))_{2} ' + \
    #                '-s$((SLURM_ARRAY_TASK_ID*' + \
    #                str(num_files_per_job) + '+{0})) -m{1}\n'

    for fetch_ind in range(math.ceil(num_files_per_job/ukbfetch_max_files)):
        files_in_fetch = min(num_files_per_job - ukbfetch_max_files*fetch_ind, ukbfetch_max_files)
        fetch_string = '${SLURM_TMPDIR}/ukbfetch' + f' -b{bulk_opt}' + f' -a{key_opt} ' + \
                       ' -o' + fetched_opt.format(fetch_ind=fetch_ind) + ' -s' + start_opt.format(ukbfetch_max_files*fetch_ind) + \
            ' -m' + num_opt.format(files_in_fetch) + '\n'
        # f.write(fetch_string.format(ukbfetch_max_files*fetch_ind, files_in_fetch, fetch_ind, localscratch))
        f.write(fetch_string)
    f.write('rm ${SLURM_TMPDIR/*')
    f.close()
    print('SLURM batch file generated; estimated completion time is {}d:{}h'.format(expected_time[0], expected_time[1]))
    return


def _convert_seconds(seconds: float) -> (int, int, int):
    """Converts seconds to d:h:m"""
    days = int(seconds/60/60/24)
    hours = int(seconds/60/60 - days*24)
    minutes = math.ceil(seconds/60 - days*24*60 - hours*60)
    return days, hours, minutes
