import tkinter
from tkinter import ttk
from tkinter import simpledialog
from course import Course

class About_Modal:
  def __init__(self, window):
    description ="""
Class Grader is a college Python project
demonstrating I/O, classes, data structures, matplotlib, and tkinter.

  Author: Thomas Bender
  Contact: tbender4@gmail.com

This software is open source and is hosted on github.com/tbender4/Class-Grader"""

    about = tkinter.Toplevel(master=window)
    about.title("Class Grader")
    # about.transient(preceding_window)   # Center original window
    #about.grab_set()                    # Modal

    msg = tkinter.Message(about, text = description)
    msg.pack()
    tkinter.Button(about, text="Close", command=about.destroy).pack()

    #size and location
    x = window.winfo_rootx()
    y = window.winfo_rooty()
    about.geometry('240x195+%d+%d' % (x,y))
    about.resizable(False, False)
    about.transient(window) #makes this a temporary button
    about.grab_set()

class New_Course(simpledialog.Dialog):                   #inherit tkinter.simpledialog
  def __init__(self, parent):
    super().__init__(parent, title="Enter Course Information:")      #inherited constructor needs original window

  def body(self, master):

    tkinter.Label(master, text="Course ID (ex: MAC108):").grid(column = 0, row=0)
    tkinter.Label(master, text="Course Full Name (ex: Intro to Python):").grid(column = 0, row=1)
    self.new_course_ID = tkinter.Entry(master)
    self.new_course_name = tkinter.Entry(master)

    self.new_course_ID.grid(column=1,row=0)
    self.new_course_name.grid(column=1,row=1)
    
    return None             

  def validate(self):
    if self.new_course_ID.get().strip() == '' or self.new_course_name.get().strip() == '':
      return 0
    return 1
  def apply(self):
    print("apply hit")
    print(str(self.new_course_ID.get()))
    self.parent.withdraw()
    course_window(self.new_course_ID.get().strip(), self.new_course_name.get().strip())

class Section_Graph:
  def __init__(self, master, section=Course('MAC000', 'test_000').sectionList[0]):
    print('generating section')
    #Have tabs for each section
    section_frame = tkinter.Frame(master)
    section_tree = ttk.Treeview(section_frame)
    section_tree.grid(row=0, column=0)
  # tkinter.Label(section_frame_test, text="i should be in the tab").grid(row=0)
    self.section_frame = section_frame
    

def new_course():
  New_Course(main_window)


def course_window(course_ID, course_name):
  def report_size(window):    #debug to report window size for testing
    print(window.winfo_width(), window.winfo_height())

  course_window=tkinter.Toplevel()

  course_window.geometry('950x800')
  # tkinter.Button(course_window, text="Report size", command=lambda: report_size(course_window)).grid(row=0)

  #Menu Bar
  menu_bar = tkinter.Menu(course_window)
  file_menu = tkinter.Menu(menu_bar, tearoff=0)
  file_menu.add_separator()
  file_menu.add_command(label="Exit", command=exit)
  menu_bar.add_cascade(label="File", menu=file_menu)
  help_menu = tkinter.Menu(menu_bar, tearoff=0)
  help_menu.add_command(label="About", command=lambda: About_Modal(course_window))    #lamba fixes arguments
  menu_bar.add_cascade(label="Help", menu=help_menu)
  course_window.config(menu=menu_bar)
  

  #generation of the course in question
  #TODO show more than one course in the GUI at the same time
  course = Course(course_ID, course_name)
  course.printCourse()

  #window elements with course:
  tkinter.Label(course_window, text = course.courseID + ' - ' + course_name, font=(None, 16)).grid(sticky='W', row=0, column= 0)


  #display all of the section info

  sections_notebook = ttk.Notebook(master=course_window)


  #Have tabs for each section

  # tkinter.Label(section_frame_test, text="i should be in the tab").grid(row=0)
  sections_notebook.add(child=Section_Graph(section_frame), text="tab_name")
  sections_notebook.grid(row=2, column=0)



main_window = tkinter.Tk()
main_window.title("Class Grader")

main_window.geometry('400x300')


new_course_button = tkinter.Button(main_window, text="New", state='normal', command=new_course)
new_course_button.grid(column=0, row=0)
label = tkinter.Label(main_window, text='Create a new course')
label.grid(column=1, row=0)

# test_button = tkinter.Button(main_window, text="test", state='normal', command=new_course)
# test_button.grid(column=0, row=1)



