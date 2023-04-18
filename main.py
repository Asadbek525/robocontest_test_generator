import os
import shutil
import sys

# get the name of the problem from args
nameOfProblem = sys.argv[1]

try:
    os.mkdir(nameOfProblem)
except OSError:
    print("Creation of the directory %s failed" % nameOfProblem)

# copy the template to the folder
shutil.copyfile("template.py", nameOfProblem + "/" + "generate.py")
shutil.copyfile("checker.py", nameOfProblem + "/" + "checker.py")
shutil.copyfile("template.cpp", nameOfProblem + "/" + "generate" + ".cpp")
shutil.copyfile("checker.cpp", nameOfProblem + "/" + "checker" + ".cpp")
shutil.copyfile("zipper.py", nameOfProblem + "/" + "zipper.py")