import os

def count_dirs_and_files(directory='.'):
    """Count the amount of of directories and files in passed in "directory" arg.
       Return a tuple of (number_of_directories, number_of_files)
    """
    dir_count = 0
    file_count = 0
    for (root, dirs, file) in os.walk(directory):
        dir_count += 1
        file_count = file_count + len(file)
    return (dir_count-1, file_count)
    pass
