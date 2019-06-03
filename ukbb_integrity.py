import os
from collections import defaultdict as dd

# These are taken from the ukb2440.bulk file, which was generated using an encoded file provided
# by UKBB and key
t1_code = '20252_2_0'
t2_code = '20253_2_0'
swi_code = '20251_2_0'
tf_code = '20249_2_0'
rf_code = '20227_2_0'
dmri_code = '20250_2_0'
checklist = [t1_code, t2_code, swi_code, tf_code, rf_code, dmri_code]

# If a subject-data pair for the codes above is in the bulk file, check for these files
t1_file = 'T1/T1.nii.gz'
t2_file = 'T2_FLAIR/T2_FLAIR.nii.gz'
swi_file = 'SWI/SWI.nii.gz'
tf_file = 'fMRI/tfMRI.nii.gz'
rf_file = 'fMRI/rfMRI.nii.gz'
dmri_file = 'dMRI/dMRI/*.nii.gz'
dmri_count = 14

def data_integrity_check(dir_master:str, bulk_file:str):
    """Function for performing sanity check that the contents of bulk data have been downloaded and unzipped.

    This function checks that T1, T2, SWI, tfMRI, rfMRI, and DWI have been downloaded and unzipped.

    Parameters
    ----------
    dir_master
        Top-level directory where subject directories are kept.
    bulk_file
        The bulk file containing a list of subject ID - datafield pairs (separated by a space, one pair per line)

    Returns
    ----------
    missing_data_dict
        Dictionary listing the missing data, keyed by subject ID.
    dat_count
        Number of files found.
    """
    # (missing_data_dict, datacount) = data_integrity_check(UK_Subject, uk_bulk_file.bulk)
    # Make code -> checker function directory
    check_func = [t1_check, t2_check, swi_check, tf_check, rf_check, dmri_check]
    check_dict = dict()
    dat_count = dd(int)
    # check_dict will take in a code and return the function which checks the code (mostly checking for existence of files)
    for c, f in zip(checklist, check_func):
        check_dict[c] = f

    # Get total number of subjects, total files found, missing
    #sub_list = os.listdir(dir_master)
    # Create subject-data pair
    sub_data = dd(list)
    missing_data_dict = dd(list)

    f = open(bulk_file, 'r')
    bulk_contents = f.readlines()
    f.close()
    for lin in bulk_contents:
        # Format is: SUBJECT DATAFIELD\n
        sub_id, dat_field = lin[:-1].split(' ')
        if(dat_field in checklist):
            sub_data[sub_id].append(dat_field)
    num_sub = len(sub_data)
    count = 0
    # For every sub_data - dat_field pair in the bulk file, do check
    for sub, dat_list in sub_data.items():
        # Directory is sub, data code is in dat_list
        for dat_code in dat_list:
            #print('{} - {}'.format(sub, dat_code))
            if(not check_dict[dat_code](sub, directory=dir_master)):
                # Data not found!
                print('Missing: {} - {}'.format(sub, dat_code))
                missing_data_dict[sub].append(dat_code)
            else:
                dat_count[dat_code] += 1
        if count % int(num_sub/100) == 0:
            print('{0:.1f}% done'.format(count / num_sub*100))
        count += 1
    return missing_data_dict, dat_count


def t1_check(subject:str, directory='./'):
    return os.path.exists(os.path.join(directory, subject, t1_file))

def t2_check(subject:str, directory='./'):
    return os.path.exists(os.path.join(directory, subject, t2_file))

def swi_check(subject:str, directory='./'):
    return os.path.exists(os.path.join(directory, subject, swi_file))

def tf_check(subject:str, directory='./'):
    return os.path.exists(os.path.join(directory, subject, tf_file))

def rf_check(subject:str, directory='./'):
    return os.path.exists(os.path.join(directory, subject, rf_file))

def dmri_check(subject:str, directory='./'):
    # Count files
    try:
        dir_list = os.listdir(os.path.join(directory, subject, 'dMRI','dMRI'))
    except FileNotFoundError:
        return False
    count = 0
    for d in dir_list:
        if('.nii.gz' in d):
            count += 1
    return count >= dmri_count
