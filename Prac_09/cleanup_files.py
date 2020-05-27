
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
    os.chdir('Lyrics/Old')

    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    # Make a new directory
    try:
        os.mkdir('temp')
    except FileExistsError:
        pass

    # Loop through each file in the (current) directory
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        modified_title_name = adjust_title_name(filename)
        modified_inside_bracket_title = adjust_inside_bracket(modified_title_name)
        new_name = get_fixed_filename(modified_inside_bracket_title)

        print("Renaming {} to {}".format(filename, new_name))

         #os.rename(filename, new_name)
         #shutil.move(filename, 'temp/' + new_name)


def adjust_title_name(name):
    """Return a file name with perfect string name"""
    # Remove the .txt part
    temp_name = name[:-4] if name.find('.') != -1 else name
    raw_name = ''
    # Add white space before capital letter
    for index, character in enumerate(temp_name):
        try:
            if character.isupper() or character == '(':
                character = ' ' + character
        except IndexError:
            pass

        raw_name += character

    # Remove white space
    pretty_name = ' '.join(raw_name.split())

    modified_name = capwords(pretty_name) + (name[-4:] if name.find('.') != -1 else '')
    # Return perfect string name
    return modified_name


def adjust_inside_bracket(filename):
    """Modify string inside bracket"""
    start = filename.find('(')
    end = filename.find(')')
    if start != -1 and end != -1:
        inside = filename[start + 1: end]
        new_inside = adjust_title_name(inside)
        filename = filename.replace(inside, new_inside)

    return filename



def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    return new_name


def demo_walk():
    """Process all subdirectories using os.walk()."""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

        # If there is any file, rename it
        if filenames:
            for filename in filenames:
                new_name = get_fixed_filename(filename)
                path = os.path.join(directory_name, filename)
                os.rename(path, new_name)


main()