import os, json
from os.path import join
from time import time
import pathlib
from shutil import copyfile
import numpy as np
from .REL_DICT import bids_dict
#bids_dict = json.load(open('UKBB_TO_REL_BIDS.json', 'r'))

def bids(dir_uk_subject=None, output_directory=None, symlink=False, overwrite=False):
    if(dir_uk_subject is None):
        raise ValueError('Specify dir_uk_subject (UK_Subject from UKBB)')
    if(output_directory is None):
        raise ValueError('Specify output directory')

    subject_dir = os.listdir(dir_uk_subject)
    num_subject = len(subject_dir)

    # Walk through top-level directory;

    time_list = np.zeros(1000)
    for ind_subject, sub in enumerate(subject_dir):
        time_start = time()
        print('Converting {}'.format(sub))
        # Create output directory
        pathlib.Path(join(output_directory, 'sub-{}'.format(sub))).mkdir(parents=True, exist_ok=True)
        # Walk through subject, copy/link to BIDS as relevant
        subject_abs_dir = join(dir_uk_subject, sub)
        for path, _, files in os.walk(subject_abs_dir):
            for fil in files:
                file_name = join(path, fil)
                bids_rel_name = get_bids_name(path, file_name)
                if(bids_rel_name is None):
                    continue
                bids_abs_name = join(output_directory, bids_rel_name)
                bids_abs_path = join(os.sep, bids_abs_name.split(os.sep)[:-1])
                pathlib.Path(bids_abs_path).mkdir(parents=True, exist_ok=True)
                exists = os.path.exists(bids_abs_name)
                if(symlink):
                    if(overwrite or not exists):
                        os.symlink(bids_abs_name, file_name)
                else:
                    if(overwrite or not exists):
                        copyfile(file_name, bids_abs_name)
        time_list[ind_subject % len(time_list)] = time() - time_start
        time_left = np.mean(time_list[:ind_subject]) * (num_subject - ind_subject - 1)
        print('Estimated time left: {0:.02f}s'.format(time_left))
        break
    return

def get_bids_name(subject, file_name):
    # Returns BIDS filename, relative to top-level directory ( OUTPUT_DIRECTORY/ )

    # Split filename according to subject
    file_split = file_name.split(subject + '/')[-1]
    try:
        bids_name = bids_dict[file_split].replace('@SUBJECT@', subject)
        return bids_name
    except KeyError:
        return None