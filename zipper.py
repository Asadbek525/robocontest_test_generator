import os
import shutil
import sys

folder_name = sys.argv[1]

def zip_folder(folder_name):
    shutil.make_archive(folder_name, 'zip', folder_name)

def main():
    zip_folder(folder_name)

if __name__ == '__main__':
    main()