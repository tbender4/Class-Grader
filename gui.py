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
    about.geometry('280x200+%d+%d' % (x,y))
    about.resizable(False, False)
    about.transient(window) #makes this a temporary button
    about.grab_set()

class New_Course(simpledialog.Dialog):                   #inherit tkinter.simpledialog
  def __init__(self, parent):
    super().__init__(parent, title="Enter Course Information:")      #inherited constructor needs original window

  def body(self, master):

    tkinter.Label(master, text="Course ID (ex: MAC108):").grid(column = 0, row=0, sticky='w')
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

class Section_Tree:   #table view
  def __init__(self, master, section=Course('MAC000', 'test_000').sectionList[0]):
    print('generating section')
    #Have tabs for each section
    
    section_tree = ttk.Treeview(master)

    #Tree view
    header_name_dict = {
      # 'student_id':'ID',
      'student_name':'Name',
      'attendance':'Attendance',
      'homework':'Homework',
      'quiz':'Quiz',
      'exam':'Exam'
    }
    section_tree['columns'] = list(header_name_dict.keys())
    for key, value in header_name_dict.items():
      section_tree.column(key, width=50)
      section_tree.heading(key, text=value)
    section_tree.heading('#0', text='ID')  #ID pertains to student ID
    section_tree.column('#0', width=40)     
    section_tree.column('attendance', width=70)
    section_tree.column('homework', width=70)
    section_tree.column('student_name', width=180)

    #inserting student to tree
    for student_grade in section.student_grade_list:
      student_ID = student_grade['student'].id
      student_name = student_grade['student'].last_first
      #b, c, and d, e should be attendances, homeworks, quizzes, exams
      section_tree.insert('', 'end', text=student_ID, values=(student_name, 'b', 'c', 'd'))


    section_tree.grid(row=0, column=0)

    #scrollbar
    # scroll = ttk.Scrollbar(section_tree, orient=tkinter.HORIZONTAL, command=section_tree.yview)
    # section_tree.configure(yscrollcommand=scroll.set)
    # scroll.grid(row=1, column=0)

    self.section_tree = section_tree
    self.section = section
  
  def add_student(self, last_name = 'test', first_name = 'name_man'):
    print('adding student')
    new_student = self.section.addStudent(last_name, first_name)
    print(new_student)
    student_id = new_student['student'].id
    name = new_student['student'].last_first
    self.section_tree.insert('', 'end', text=student_id, values=(name, 'n', 'o', 'p'))
    

def new_course():
  New_Course(main_window)

def test_course():
  course_window('MAC000', 'Intro to Testing')


def course_window(course_ID, course_name):
  def report_size(window):    #debug to report window size for testing
    print(window.winfo_width(), window.winfo_height())

  def add_new_section(notebook, course):
    child = Section_Tree(notebook, course.addNewSection()).section_tree
    text = course.courseID + '-' + "{:02d}".format(course.sectionList[-1].sectionID)
    
    notebook.add(child=child, text=text)
    
  
  #generation of the course in question
  #TODO show more than one course in the GUI at the same time
  course = Course(course_ID, course_name)
  course.printCourse()

  course_window=tkinter.Toplevel()
  course_window.geometry('950x800')

  #Menu Bar
  menu_bar = tkinter.Menu(course_window)
  file_menu = tkinter.Menu(menu_bar, tearoff=0)
  file_menu.add_separator()
  file_menu.add_command(label="Exit", command=main_window.destroy)
  menu_bar.add_cascade(label="File", menu=file_menu)
  help_menu = tkinter.Menu(menu_bar, tearoff=0)
  help_menu.add_command(label="About", command=lambda: About_Modal(course_window))    #lamba fixes arguments
  menu_bar.add_cascade(label="Help", menu=help_menu)
  course_window.config(menu=menu_bar)
  

  #window elements with course:
  tkinter.Label(course_window, text = course.courseID + ' - ' + course_name, font=(None, 16)).grid(sticky='W', row=0, column= 0)


  #display all of the section info
  sections_notebook = ttk.Notebook(master=course_window)

  #Have tabs for each section 

  for section in course.sectionList:
    section_frame = tkinter.Frame(sections_notebook)
    section_tree = Section_Tree(section_frame, section)
    section_tree.section_tree.grid(row=0, column=0)
    sections_notebook.add(child=section_frame, text=course.courseID + '-' + "{:02d}".format(course.sectionList[-1].sectionID))
    add_student = tkinter.Button(section_frame, text='Add Student', command=lambda: section_tree.add_student())
    add_student.grid(row=1, column=0)
    
    


  #placing course_window grid
  tkinter.Button(course_window, text="Report size",
                 command=lambda: report_size(course_window)).grid(row=1, sticky='W')
  add_button = tkinter.Button(course_window, text="Add Section",
                 command=lambda: add_new_section(sections_notebook, course))
  add_button.grid(column=1, row=1, sticky='W')

  sections_notebook.grid(row=2, columnspan=2, sticky='se') #colspan is dirty button spacing fix





main_window = tkinter.Tk()
main_window.title("Class Grader")
main_window.geometry('400x300')


new_course_button = tkinter.Button(main_window, text="New", state='normal', command=new_course)
test_course_button = tkinter.Button(main_window, text="Test", state='normal', command=test_course)
new_course_button.grid(column=0, row=0)
test_course_button.grid(column=0, row=1)
label = tkinter.Label(main_window, text='Create a new course')
label.grid(column=1, row=0)

# test_button = tkinter.Button(main_window, text="test", state='normal', command=new_course)
# test_button.grid(column=0, row=1)



