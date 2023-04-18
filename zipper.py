import os
import shutil
import sys


def zip_test_cases():
    shutil.make_archive("tests", "zip", "tests")


def main():
    zip_test_cases()


if __name__ == '__main__':
    main()
