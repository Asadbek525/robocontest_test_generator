import os
import shutil


nameOfProblem = input("Enter the name of the problem: ").replace(" ", "_").lower()

try:
    os.mkdir(nameOfProblem)
except OSError:
    print("Creation of the directory %s failed" % nameOfProblem)

# copy the template to the folder
shutil.copyfile("template.py", nameOfProblem + "/" + "_py.py")
shutil.copyfile("checker.py", nameOfProblem + "/" + "_checker.py")
shutil.copyfile("template.cpp", nameOfProblem + "/" + "_cpp" + ".cpp")
shutil.copyfile("checker.cpp", nameOfProblem + "/" + "_checker" + ".cpp")

