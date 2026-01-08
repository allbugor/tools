import shutil

from .copy_tools import copy_files_meta
# ! Top-Down func definitions

def zip_archive(destination, target, *, is_files_list=False, delete_target=False):
    if is_files_list:
        target = copy_files_meta(destination, target)

    shutil.make_archive(destination, "zip", target)
    
    if delete_target:
        shutil.rmtree(target)
    
    return destination + ".zip"