import tkinter
from tkinter import ttk
from tkinter import simpledialog
from course import Course
from section import Section

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
    tkinter.Button(about, text="Close", command=about.destroy)

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
    # self.parent.withdraw()
    course_window(self.new_course_ID.get().strip(), self.new_course_name.get().strip())

class New_Student(simpledialog.Dialog):  # inherit tkinter.simpledialog
  def __init__(self, parent):
    # inherited constructor needs original window
    super().__init__(parent, title="Enter Student Information:")

  def body(self, master):

    tkinter.Label(master, text="Last Name").grid(
        column=0, row=0, sticky='w')
    tkinter.Label(master, text="First Name:").grid(
        column=0, row=1)
    self.last_name_entry = tkinter.Entry(master)
    self.first_name_entry = tkinter.Entry(master)

    self.last_name_entry.grid(column=1, row=0)
    self.first_name_entry.grid(column=1, row=1)

    return None

  def validate(self):
    if self.last_name_entry.get().strip() == '' or self.first_name_entry.get().strip() == '':
      return 0
    return 1

  def apply(self):
    print("apply hit")

    self.last_name = self.last_name_entry.get().strip()
    self.first_name = self.first_name_entry.get().strip()

class Section_Tree(ttk.Treeview):   #table view. possibly rewrite with inheritance
  def __init__(self, master, section=Course('MAC000', 'test_000').sectionList[0]):
    # self.section_tree = section_tree
    self.section = section
    self.master = master
    self.student_grade_list = self.section.student_grade_list
    super().__init__(master)
    # def add_student_section(self, last_name='test', first_name='name_man'):
    #   print('adding student')
    #   new_student = self.section.addStudent(last_name, first_name)
    #   print(new_student)
    #   student_id = new_student['student'].id
    #   name = new_student['student'].last_first
    #   self.section_tree.insert('', 'end', text=student_id, values=(name, 'n', 'o', 'p'))
    # section_tree = ttk.Treeview(master)

    #Tree view

    #formatting columns
    header_name_dict = {
        # 'student_id':'ID',
        'student_name': 'Name',
        'attendance': 'Attendance',
        'homework': 'Homework',
        'quiz': 'Quiz',
        'exam': 'Exam'
    }
    self['columns'] = list(header_name_dict.keys())
    for key, value in header_name_dict.items():
      self.column(key, width=50)
      self.heading(key, text=value)
    self.heading('#0', text='ID')  #ID pertains to student ID
    self.column('#0', width=40)     
    self.column('attendance', width=70)
    self.column('homework', width=70)
    self.column('student_name', width=180)

    #inserting existing values from section
    for student_grade in self.student_grade_list:
      a, b, text, values = self.gen_child(student_grade) 
      #b, c, and d, e should be attendances, homeworks, quizzes, exams
      self.insert(a, b, text=text, values=values)


  def gen_child(self, student_grade, last_name = None, first_name = None):
    print(student_grade)

    student_ID = student_grade['student'].student_id
    student_last = student_grade['student'].last_name
    student_first = student_grade['student'].first_name
    student_last_first = student_grade['student'].last_first
    #if options are provided, overwrite info with given info (should reflect in data as well)
    if last_name != None and first_name != None:
      student_last = last_name
      student_first = first_name
      student_grade['student'].updateLF()
      student_last_first = student_grade['student'].last_first # possibly redundant

    return ('', 'end', student_ID, (student_last_first , 'a', 'b', 'c', 'd'))
  
  def add_student(self, last_name = 'test', first_name = 'name_man'):
    # first gets the info. Then adds it to the section. then inserts the data into the tree.
    # it's possible that the data may be reconstructed. so it's properly synced (need to decide best route)

    # new_student = New_Student(self.master)
    new_student = New_Student(self)

    last_name = new_student.last_name
    first_name = new_student.first_name
    print('adding student:', last_name, first_name)
    new_student_grade = self.section.addStudentGrade(last_name, first_name)  #this adds a student_grade, not Student
    print(new_student_grade)

    a, b, text, values = self.gen_child(new_student_grade, last_name, first_name)
    self.insert(a, b, text=text, values=values)

  def edit_student(self):
    # TODO: Have the whole student_grade be stored as a hidden value

    focus = self.focus()
    # print(focus[]

    #this is dirty. doesn't save information properly
    #Having the student as an argument would be best student would be best
    l_f = self.item(focus)['values'][0].split(",")
    last = l_f[0]
    first = l_f[1]
    print('test', l_f)


    new_student = Edit_Student(self.master, last, first)
    last_first = new_student.last_name + ', ' + new_student.first_name
    self.item(focus, values=(last_first, new_student.att_avg, new_student.hw_avg, new_student.exam_avg, new_student.quiz_avg))
    print(self.item(self.focus()))

class Edit_Student(simpledialog.Dialog):  # inherit tkinter.simpledialog
  def __init__(self, parent, last_name='l', first_name='f'):
    # inherited constructor needs original window
    self.last_name = last_name
    self.first_name = first_name
    super().__init__(parent, title="Edit Student Information:")

  def body(self, master):

    tkinter.Label(master, text="Last Name").grid(
        column=0, row=0, sticky='e')
    tkinter.Label(master, text="First Name:").grid(
        column=0, row=1, sticky='e')
    print(self.last_name, self.first_name)
    self.last_name_entry = tkinter.Entry(master)
    self.last_name_entry.insert(0, self.last_name)
    self.first_name_entry = tkinter.Entry(master)
    self.first_name_entry.insert(0, self.first_name)

    self.last_name_entry.grid(column=1, row=0)
    self.first_name_entry.grid(column=1, row=1)

    tkinter.Label(master, text="Attendance\n(0 for absent, 1 for present):").grid(row=2)
    tkinter.Label(master, text="Homework:\n(from 0 - 100)").grid(row=2, column=1)
    tkinter.Label(master, text="Quiz:\n(from 0 - 100)").grid(row=2, column=2)
    tkinter.Label(master, text="Exam:\n(from 0 - 100)").grid(row=2, column=3)

    self.att_entry = []
    for i in range(3,15):
      entry = tkinter.Entry(master)
      entry.insert(0, '0')
      entry.grid(row=i, column = 0)
      self.att_entry.append(entry)

    self.hw_entry = []
    for i in range(3, 15):
      entry = tkinter.Entry(master)
      entry.insert(0, '0')
      entry.grid(row=i, column=1)
      self.hw_entry.append(entry)

    self.quiz_entry = []
    for i in range(3, 15):
      entry = tkinter.Entry(master)
      entry.insert(0, '0')
      entry.grid(row=i, column=2)
      self.quiz_entry.append(entry)


    self.exam_entry = []
    for i in range(3, 7):
      entry = tkinter.Entry(master)
      entry.insert(0, '0')
      entry.grid(row=i, column=3)
      self.exam_entry.append(entry)

    return None

  def validate(self):
    try:
      for entry in self.att_entry:
        value = int(entry.get().strip())
        if value > 1 or value < 0:
          return 0
      for entry in self.hw_entry:
        value = int(entry.get().strip())
        if value > 100 or value < 0:
          return 0
      for entry in self.quiz_entry:
        value = int(entry.get().strip())
        if value > 100 or value < 0:
          return 0
      for entry in self.exam_entry:
        value = int(entry.get().strip())
        if value > 100 or value < 0:
          return 0

    except ValueError:
      return 0

    if self.last_name_entry.get().strip() == '' or self.first_name_entry.get().strip() == '':
      return 0

    return 1

  def apply(self):
    print("apply hit")

    self.last_name = self.last_name_entry.get().strip()
    self.first_name = self.first_name_entry.get().strip()
    
    self.att_avg = 100 # reports back as percentage
    att_sum = 0
    for i in self.att_entry:
      att_sum += int(i.get().strip())
      print(att_sum)
    self.att_avg = str(round(att_sum / len(self.att_entry) * 100, 2))+"%"
    
    hw_sum = 0
    for i in self.hw_entry:
      hw_sum += int(i.get().strip()) / 100
    self.hw_avg = str(round(hw_sum / len(self.hw_entry) * 100, 2))+"%"

    quiz_sum = 0
    for i in self.quiz_entry:
      quiz_sum += int(i.get().strip()) / 100
    self.quiz_avg = str(round(quiz_sum / len(self.quiz_entry) * 100, 2))+"%"

    exam_sum = 0
    for i in self.exam_entry:
      exam_sum += int(i.get().strip()) / 100
    self.exam_avg = str(round(exam_sum / len(self.exam_entry) * 100, 2))+"%"

class Section_Frame(tkinter.Frame):
  # ---------------------
  #   ----------------
  #   |              |
  #   |     Tree     |
  #   |              |
  #   ----------------
  #     |add| |edit|
  # 
  # ---------------------

  def __init__(self, master, section = Section()):
    super().__init__(master)
    section_tree = tkinter.Label(self, text='Tree here')  #Replace this with Section_Tree
    add_button = tkinter.Button(self, text='Add Student')
    edit_button = tkinter.Button(self, text='Edit Student')

    section_tree.grid(row=0,columnspan=2)
    add_button.grid(row=1, column = 0)
    edit_button.grid(row=1, column=1)
    # tkinter.Label(self, text='Custom frame').grid(row=0)


def new_course():
  New_Course(main_window)

def test_course():
  course_window('MAC000', 'Intro to Testing')


def course_window(course_ID, course_name):
  def report_size(window):    #debug to report window size for testing
    print(window.winfo_width(), window.winfo_height())

  def add_new_section(notebook, course):
    s_frame = Section_Frame(notebook, course.addNewSection())
    frame = tkinter.Frame(notebook)
    s_tree = Section_Tree(frame, course.addNewSection())
    tree = s_tree  #actual tree widget
    tree.grid(row=0, columnspan=2)

    add_student = tkinter.Button(
        frame, text='Add Student', command=lambda: s_tree.add_student())

    edit_student = tkinter.Button(frame, text = 'Edit Student', command=lambda: s_tree.edit_student())

    print_section = tkinter.Button(
        frame, text='Print Section', command=lambda: s_tree.section.printSection())

    add_student.grid(row=1, column=0)
    edit_student.grid(row=1, column=1)

    text = course.courseID + '-' + "{:02d}".format(course.sectionList[-1].sectionID)
    # notebook.add(child=frame, text=text)
    notebook.add(child=s_frame, text=text)
    
  
  #generation of the course in question
  #TODO show more than one course in the GUI at the same time
  course = Course(course_ID, course_name)
  course.printCourse()

  course_window=tkinter.Toplevel()
  course_window.geometry('540x400')

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
  #Generate tables from current list

  #perhaps pass through the whole section
  for section in course.sectionList:
    section_frame = tkinter.Frame(sections_notebook)
    section_tree = Section_Tree(section_frame, section)
    section_tree.grid(row=0, columnspan=2)
    sections_notebook.add(child=section_frame, text=course.courseID + '-' + "{:02d}".format(course.sectionList[-1].sectionID))
    add_student = tkinter.Button(section_frame, text='Add Student', command=lambda: section_tree.add_student())
    edit_student = tkinter.Button(
        section_frame, text='Edit Student ', command=lambda: section_tree.edit_student())
    add_student.grid(row=1, column=0)
    edit_student.grid(row=1, column = 1)
    
    


  #placing course_window grid
  tkinter.Button(course_window, text="Report size",
                 command=lambda: report_size(course_window)).grid(row=1, sticky='W')
  add_button = tkinter.Button(course_window, text="Add Section",
                 command=lambda: add_new_section(sections_notebook, course))
  add_button.grid(column=1, row=1, sticky='W')


  # colspan is dirty button spacing fix
  sections_notebook.grid(row=2, columnspan=2, sticky='NS')

  tkinter.Button(course_window, text='Print Course',
                 command=course.printCourse).grid(row=3, sticky='w')


main_window = tkinter.Tk()
main_window.title("Class Grader")
main_window.geometry('400x300')

new_course_button = tkinter.Button(main_window, text="New", state='normal', command=new_course)
test_course_button = tkinter.Button(main_window, text="Test", state='normal', command=test_course)
new_course_button.grid(column=0, row=0)
test_course_button.grid(column=0, row=1)
label = tkinter.Label(main_window, text='Create a new course')
label.grid(column=1, row=0)

testLabel = Section_Frame(main_window)
testLabel.grid(row=2)

# test_button = tkinter.Button(main_window, text="test", state='normal', command=new_course)
# test_button.grid(column=0, row=1)



