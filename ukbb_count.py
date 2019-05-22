import os
from collections import defaultdict as dd

def total_file_count(directory):
    sub_list = os.listdir(directory)
    # Go through subject list
    file_count_list = []
    for sub in sub_list:
        # Confirm that item is directory (may cause problems if non-subject directories are present)
        if(os.path.isdir(os.path.join(directory,sub))):
            file_count = 0
            for d in os.walk(os.path.join(directory,sub)):
                file_count += len(d[-1])
            file_count_list.append(file_count)
    return file_count_list
