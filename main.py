# IMPORTANT: matplotlib is required.
# matplotlib is part of Anaconda but it can also be installed manually.
# macOS install: python3 -m pip install -U matplotlib
# Windows install: py -m pip install -U matplotlib

import tkinter
from course import Course
# import student
#import matplotlib

"""
ideas:
create a grading database application 
start with simple proof of concept classes. output via terminal.
then integrate tkinter
then integrate matplotlib

use json to store files. json plays with dictionaries
"""


print("hello")
myCourse = Course(101, "Intro to CS")
myCourse.addNewSection()
myCourse.sectionList[0].addStudent()
myCourse.printCourse()

mainGUI = tkinter.Tk()
mainGUI.mainloop()
