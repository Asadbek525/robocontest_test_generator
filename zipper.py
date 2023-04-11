import os
import shutil
import sys


def zip_test_cases():
    # zip all .in and .out files in the current directory
    # and put them in a folder called test_cases
    # and then zip the folder
    # and then delete the folder

    # create the folder
    try:
        os.mkdir("test_cases")
    except OSError:
        print("Creation of the directory %s failed" % "test_cases")

    # copy all .in and .out files to the folder
    for file in os.listdir():
        if file.endswith(".in") or file.endswith(".out"):
            shutil.copyfile(file, "test_cases/" + file)

    # zip the folder
    shutil.make_archive("_test_cases", "zip", "test_cases")

    # delete the folder
    shutil.rmtree("test_cases")


def main():
    zip_test_cases()


if __name__ == '__main__':
    main()
