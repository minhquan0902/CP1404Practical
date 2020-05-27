"""
CP1404/CP5632 Practical
Demos of various os module examples
Github link: https://github.com/minhquan0902/CP1404Practical
"""

import shutil
import os
from string import capwords


def main():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('FilesToSort')

    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))
    filenames = os.listdir('.')
    endings = [filename[filename.find('.') + 1:] for filename in filenames if filename.find('.') != -1]
    clean_endings = [ending for index, ending in enumerate(endings) if ending not in endings[:index]]
    clean_endings.sort()
    print(clean_endings)
    directories = {}

    for ending in clean_endings:
        directory = input('What category would you like to sort {} files into? '.format(ending))
        directories[directory] = [] if directory not in directories.keys() else directories[directory]
        directories[directory].append(ending)

    for filename in filenames:
        move_file(filename, directories)


def move_file(filename, directories):
    dot_index = filename.find('.')
    ending = filename[dot_index + 1:] if dot_index != -1 else None
    try:
        for directory in directories.keys():
            print(directory)
            os.mkdir(directory)
    except:
        pass
    if ending:
        output_directory = ''
        for key, value in directories.items():
            if ending in value:
                output_directory = key

        shutil.move(filename, output_directory + '/' + filename)


main()
