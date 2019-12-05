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

def subwindow():
  sub_window=tkinter.Tk()
  sub_window.mainloop()
# print("hello")
# myCourse = Course(101, "Intro to CS")
# myCourse.addNewSection()
# myCourse.sectionList[0].addStudent()
# myCourse.printCourse()


main_window = tkinter.Tk()
main_window.title("Class Grader")

main_window.geometry('400x300')

new_course_button = tkinter.Button(main_window, text="New", state='normal', command=subwindow)
new_course_button.grid(column=0, row=0)
label = tkinter.Label(main_window, text='Create a new course')
label.grid(column=1, row=0)


main_window.mainloop()