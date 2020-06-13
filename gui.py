import tkinter
from tkinter import ttk
from tkinter import simpledialog
from tkinter import messagebox
from course import Course
from section import Section
import grading  ##for attendance_date related


class About_Dialog(simpledialog.Dialog):
  def __init__(self, parent, title="Class Grader"):
    super().__init__(parent, title=title)
  
  def body (self, master):

    description ="""
Class Grader is a college Python project
demonstrating I/O, classes, data structures, matplotlib, and tkinter.

  Author: Thomas Bender
  Contact: tbender4@gmail.com

This software is open source and is hosted on github.com/tbender4/Class-Grader"""

    tkinter.Label(master, text=description).grid(column=0, row=0)
    return master
    

  def buttonbox(self):
    # Similar to stock but ONLY a close button
    box = tkinter.Frame(self)
    w = tkinter.Button(box, text="Close", width=10, command=self.cancel)
    w.pack(side=tkinter.LEFT, padx=5, pady=5)
    self.bind("<Return>", self.ok)
    self.bind("<Escape>", self.cancel)
    box.pack()

  

class New_Course(simpledialog.Dialog):                   #inherit tkinter.simpledialog
  def __init__(self, parent, test = False):
    self.test = test
    super().__init__(parent, title="Enter Course Information:")      #inherited constructor needs original window
    




  def body(self, master):
    def update_status():
      for days in self.days_toggle:
        print(days.get())
      isValid, message = grading.attendance_date_range_dryrun(self.days_toggle, self.from_entry.get(), self.to_entry.get())
      print(message)
      message_var.set(message)

    info_frame = tkinter.Frame(master)
    info_frame.grid(column=0, row=0, columnspan=2)
    tkinter.Label(info_frame, text="Course ID (ex: MAC108):").grid(column = 0, row=0, sticky='w')
    tkinter.Label(info_frame, text="Course Full Name (ex: Intro to Python):").grid(column = 0, row=1)
    self.new_course_ID = tkinter.Entry(info_frame)
    self.new_course_name = tkinter.Entry(info_frame)
    self.new_course_ID.grid(column=1,row=0)
    self.new_course_name.grid(column=1,row=1)

    range_frame = tkinter.Frame(master)
    range_frame.grid(row=1, column=0)

    tkinter.Label(range_frame, text="Range (mm/dd/yy):").grid(row=0, column = 0)
    tkinter.Label(range_frame, text="From:").grid(row=0, column = 1)
    self.from_entry = tkinter.Entry(range_frame, width=8)
    self.from_entry.grid(row = 0, column = 2)
    tkinter.Label(range_frame, text="To:").grid(row=0, column = 3)
    self.to_entry = tkinter.Entry(range_frame, width=8)
    self.to_entry.grid(row = 0, column = 4)

    days_frame = tkinter.Frame(master)
    days_frame.grid(row=2, column=0)
    days_of_week = ['M', 'Tu', 'W', 'Th', 'F', 'Sa', 'Su']
    self.days_toggle = []
    self.checkbuttons = []
    for i in range(7):
      self.days_toggle.append(tkinter.BooleanVar(master))
      checkbutton = tkinter.Checkbutton(days_frame, text=days_of_week[i], variable=self.days_toggle[i])
      checkbutton.grid(row=0, column=i)

      self.checkbuttons.append(checkbutton)
      
    verify_button = tkinter.Button(days_frame, text="Verify", command=update_status)
    verify_button.grid(row= 0, column = 8)

    message_var = tkinter.StringVar(master)
    message_var.set("Press Verify to check status")
    message_label = tkinter.Label(days_frame, textvariable=message_var, wraplength=240)
    message_label.grid(row=1, column=0, columnspan=9)

    if self.test:
      self.new_course_ID.insert(0, 'MAC000')
      self.new_course_name.insert(0, 'Intro to Testing')
      self.from_entry.insert(0, '05/05/19')
      self.to_entry.insert(0, '08/08/19')
      self.checkbuttons[0].select()
      self.checkbuttons[2].select()
    
    return None             

  def validate(self):
    if self.new_course_ID.get().strip() == '' or self.new_course_name.get().strip() == '':
      return 0
    

    status = 0
    for days in self.days_toggle:
      if days.get():
        status = 1
        break
    
    if not status:
      return 0

    return grading.attendance_date_range_dryrun(self.days_toggle, self.from_entry.get(), self.to_entry.get())[0]


  def apply(self):
    print("apply hit")
    print(str(self.new_course_ID.get()))
    # self.parent.withdraw()  
    # TODO: Save this to the actual course data. Then draw window.
    attendance_date_template = grading.attendance_date_range(self.days_toggle, self.from_entry.get(), self.to_entry.get())

    course_window(self.new_course_ID.get().strip(), self.new_course_name.get().strip(), attendance_date_template)

class New_Student_Dialog(simpledialog.Dialog):  # inherit tkinter.simpledialog
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

    self.tree_student_dict = {}
    # insertion_ID : student_grade
    # insertion_ID is focusable. This syncs the insertionID with the student data
    #

    #inserting existing values from section
    for student_grade in self.student_grade_list:
      a, b, text, values = self.gen_child(student_grade) 
      #b, c, and d, e should be attendances, homeworks, quizzes, exams
      insertion_ID = self.insert(a, b, text=text, values=values)
      self.tree_student_dict.update({insertion_ID : student_grade})

  def gen_child(self, student_grade, last_name = None, first_name = None):

    #if options are provided, overwrite info with given info (should reflect in data as well)
    if last_name != None and first_name != None:
      student_grade['student'].last_name = last_name
      student_grade['student'].first_name = first_name
      student_grade['student'].updateLF()
    student_ID = student_grade['student'].student_id
    student_last = student_grade['student'].last_name #unused so far.
    student_first = student_grade['student'].first_name #unused so far.
    student_last_first = student_grade['student'].last_first

    #idea 06/07: pass through the whole object rather than renaming.
    #unsure why I added them individually.
    #    
    
    return ('', 'end', student_ID, (student_last_first , 'a', 'b', 'c', 'd'))
  
  def add_student(self, last_name = 'test', first_name = 'name_man'):
    # first gets the info. Then adds it to the section. then inserts the data into the tree.
    # it's possible that the data may be reconstructed. so it's properly synced (need to decide best route)

    # new_student = New_Student(self.master)
    new_student = New_Student_Dialog(self)

    last_name = new_student.last_name
    first_name = new_student.first_name
    print('adding student:', last_name, first_name)
    new_student_grade = self.section.addStudentGrade(last_name, first_name)  #this adds a student_grade, not Student
    
    a, b, text, values = self.gen_child(new_student_grade, last_name, first_name)

    insertion_ID = self.insert(a, b, text=text, values=values)
    self.tree_student_dict.update({insertion_ID : new_student_grade})


  def edit_student(self):
    # TODO: Merge this with the Edit_Student class so the code is cleaner

    focus = self.focus()  #gets the item ID. need to put into self.item to be usable
    print("printing focus: "+ focus)
    student_grade = self.tree_student_dict[focus]   # Incredibly important line. Allows the original data to reflect what's in the GUI

    # UPDATE 04/23/20: It syncs properly now! Using tree_student_dict!!

    new_student = Edit_Student(self.master, student_grade)  #passes in existing student_grade
    #section is passed through to utilize the section's template of attendances.

    # 06/07: I believe the strategy is: create a variable inside new_student. then update this function's student_grade with that information. Then
    #will later implement the score related information
    # 06/07 part 2: I'm learning how important it is to be aware of pass by reference... code is simple now.


    # takes info and determines what's the outward facing information.
    # TODO: the below outputs. I probably should make this functions in the student class.
    # att_avg
    # hw_avg
    # exam_avg
    # quiz_avg
    #end of outward facing information.
    
    self.item(focus, values=(student_grade['student'].last_first, 'new_student.att_avg', 'new_student.hw_avg', 'new_student.exam_avg', 'new_student.quiz_avg'))
    print(self.item(self.focus()))

class Edit_Student(simpledialog.Dialog):  # inherit tkinter.simpledialog
  class Attendance_Tree(ttk.Treeview):
    def __init__ (self, master, student_grade):
      super().__init__(master)

      self.attendances = student_grade['attendances']

      #formatting
      header_names = {
        #'date' : 'Date',
        'attendance' : 'Attendance'
      }
      self['columns'] = list(header_names.keys())
      for key, value in header_names.items():
        # self.column(key, width = 40)
        self.heading(key, text=value)

      self.column('#0', width = 80)
      self.heading('#0', text = 'Date')

      self.tree_attendance_dict = {}  #similar to edit_student's strategy of syncing data

      #inserting values
      for attendance in student_grade['attendances']:
        value = ''
        if attendance.day_status != -1:
          value = grading.Attendance.descriptions[attendance.day_status]
        insertion_ID = self.insert('', 'end', text=attendance.date, values = (value))
        self.tree_attendance_dict.update({insertion_ID : attendance})

    def update_overall_att_grade_string_var(self, output_string):
      # returns raw overall grade and associated grade letter.
      # grade letter conversion should be a function found in grading.
      # have button to change this policy.
      avg = grading.Attendance.attendance_generate_grade(self.attendances)
      letter_grade = grading.letter_grade(avg)

      output_string.set('Current Grade: {}, {}'.format(letter_grade, avg))

    def edit_attendance(self):
      attendance = self.tree_attendance_dict[self.focus()]
      print(attendance.day_status, attendance.date)
      #attendance.printAttendance()  #TODO: Create edit dialog

    def print_focus(self):
      print(self.item(self.focus()))

    def gen_att_optmenu(self, master):
      descriptions = grading.Attendance.descriptions
      # attendance = self.tree_attendance_dict[self.focus()]
      self.output = tkinter.StringVar(master)

      self.output.set('')
      optmenu = tkinter.OptionMenu(master, self.output, *descriptions)
      
      self.output.trace('w', self.update_att)

      self.update_overall_att_grade_string_var(self.output)
      return optmenu
    
    def update_att(self, *args):
      attendance = self.tree_attendance_dict[self.focus()]
      index = grading.Attendance.descriptions.index(self.output.get())

      attendance.day_status = index

      self.item(self.focus(), values=(self.output.get()))

  class Score_Tree(ttk.Treeview):
    #Abstract. Use the below tress instead
    #TODO: Possibly re-combine and have passed through inits change the header and key?
    def __init__ (self, master, student_grade):
      super().__init__(master)

      #formatting
      header_names = {
        #'homework_number' : 'Homework Number',
        'grade' : 'Grade',
        'use_curve' : "Grade Type",
        'description' : 'Description'
      }
      self['columns'] = list(header_names.keys())
      for key, value in header_names.items():
        # self.column(key, width = 40)
        self.heading(key, text=value)

      self.column('#0', width = 80)

  class Homework_Tree(Score_Tree):
    def __init__ (self, master, student_grade):
      super().__init__(master, student_grade)
      self.heading('#0', text = 'HW Number')

      #inserting values
      for homework in student_grade['homeworks']:
        self.insert('', 'end', text=homework.score_id, values = (homework.description, homework.get_score(), homework.use_curve))
        # TODO: Score needs to be a function that responds to whether to show raw score or curved score.
    
  class Quiz_Tree(Score_Tree):
    def __init__ (self, master, student_grade):
      super().__init__(master, student_grade)
      self.heading('#0', text = 'Quiz Number')

      #inserting values
      for quiz in student_grade['quizzes']:
        self.insert('', 'end', text=quiz.score_id, values = (quiz.description, 'N/100', quiz.use_curve))
        # TODO: Score needs to be a function that responds to whether to show raw score or curved score.
  
  class Exam_Tree(Score_Tree):
    def __init__ (self, master, student_grade):
      super().__init__(master, student_grade)
      self.heading('#0', text = 'Exam Number')

      #inserting values
      for exam in student_grade['exams']:
        self.insert('', 'end', text=exam.score_id, values = (exam.description, 'N/100', exam.use_curve))
        # TODO: Score needs to be a function that responds to whether to show raw score or curved score.


  def __init__(self, parent, student_grade):
    # inherited constructor needs original window
    self.student_grade = student_grade
    self.last_name = self.student_grade['student'].last_name
    self.first_name = self.student_grade['student'].first_name  #this is of type string. this is probably why it's pass by value and gave me the headache
    super().__init__(parent, title="Edit Student Information:")

  def body(self, master):
    def print_selected_attendance():
      attendance_tree.edit_attendance()

    
    name_frame = tkinter.Frame(master)
    name_frame.grid(row = 0, column = 0, rowspan = 2, columnspan = 2)

    tkinter.Label(name_frame, text="Last Name").grid(
        column=0, row=0, sticky='e')
    tkinter.Label(name_frame, text="First Name:").grid(
        column=0, row=1, sticky='e')
    self.last_name_entry = tkinter.Entry(name_frame)
    self.last_name_entry.insert(0, self.last_name)
    self.first_name_entry = tkinter.Entry(name_frame)
    self.first_name_entry.insert(0, self.first_name)

    self.last_name_entry.grid(column=1, row=0)
    self.first_name_entry.grid(column=1, row=1)

    att_frame = tkinter.Frame(master)
    att_frame.grid(row=2, column = 0, columnspan=2)
    attendance_tree = self.Attendance_Tree(att_frame, self.student_grade)
    attendance_tree.grid(row=0, column=0, columnspan=2)
    tkinter.Label(att_frame, text='Change Status to:').grid(row=1, column=0)
    att_optmenu = attendance_tree.gen_att_optmenu(att_frame)
    att_optmenu.grid(row=1, column=1)

    
    self.att_grade_msg = tkinter.StringVar(master)
    self.att_grade_msg.set('')
    att_grade = tkinter.Label(att_frame, text=self.att_grade_msg)
    att_grade.grid(row=2, column=0, columnspan=2)

    # edit_attendance_button = tkinter.Button(master, text='Print Selected Attendance', command=print_selected_attendance)
    # edit_attendance_button.grid(row=3, column=0, columnspan=2)
    #TODO: Implement DUMMY

    homework_tree = self.Homework_Tree(master, self.student_grade)
    homework_tree.grid(row=2, column = 2, columnspan=2)
    add_hw_button = tkinter.Button(master, text = 'Add New HW')
    edit_hw_button = tkinter.Button(master, text = 'Edit Selected HW')
    add_hw_button.grid(row=3, column=2)
    edit_hw_button.grid(row=3, column=3)

    quiz_tree = self.Quiz_Tree(master, self.student_grade)
    quiz_tree.grid(row=4, column = 0, columnspan=2)
    exam_tree = self.Exam_Tree(master, self.student_grade)
    exam_tree.grid(row=4, column = 2, columnspan=2)
    #TODO: GUI HW only; untested.


    # tkinter.Label(master, text="Attendance\n(0 for absent, 1 for present):").grid(row=2)
    # tkinter.Label(master, text="Homework:\n(from 0 - 100)").grid(row=2, column=1)
    # tkinter.Label(master, text="Quiz:\n(from 0 - 100)").grid(row=2, column=2)
    # tkinter.Label(master, text="Exam:\n(from 0 - 100)").grid(row=2, column=3)

    # self.att_entry = []

    # for i, attendance in enumerate([1, 2, 3, 4, 5], start=3):
    #   entry = tkinter.Entry(master)
    #   entry.insert(0, attendance)
    #   entry.grid(row=i, column = 0)
    #   self.att_entry.append(entry)
    # print("outside:", i)
    # last_i = i
    # button = tkinter.Button(master, text="Add new attendance", command=lambda: addEntry(last_i+1, self.att_entry, button))
    # button.grid(row=last_i+1, column=0)

    # self.hw_entry = []
    # for i in range(3, 15):
    #   entry = tkinter.Entry(master)
    #   entry.insert(0, '0')
    #   entry.grid(row=i, column=1)
    #   self.hw_entry.append(entry)

    # self.quiz_entry = []
    # for i in range(3, 15):
    #   entry = tkinter.Entry(master)
    #   entry.insert(0, '0')
    #   entry.grid(row=i, column=2)
    #   self.quiz_entry.append(entry)


    # self.exam_entry = []
    # for i in range(3, 7):
    #   entry = tkinter.Entry(master)
    #   entry.insert(0, '0')
    #   entry.grid(row=i, column=3)
    #   self.exam_entry.append(entry)

    return None

  def validate(self):
    # try:
    #   for entry in self.att_entry:
    #     value = int(entry.get().strip())
    #     if value > 1 or value < 0:
    #       return 0
    #   for entry in self.hw_entry:
    #     value = int(entry.get().strip())
    #     if value > 100 or value < 0:
    #       return 0
    #   for entry in self.quiz_entry:
    #     value = int(entry.get().strip())
    #     if value > 100 or value < 0:
    #       return 0
    #   for entry in self.exam_entry:
    #     value = int(entry.get().strip())
    #     if value > 100 or value < 0:
    #       return 0

    # except ValueError:
    #   return 0

    if self.last_name_entry.get().strip() == '' or self.first_name_entry.get().strip() == '':
      return 0

    return 1

  def apply(self):
    print("apply hit")

    self.student_grade['student'].last_name = self.last_name_entry.get().strip()
    self.student_grade['student'].first_name = self.first_name_entry.get().strip()
    self.student_grade['student'].updateLF()
    
    # self.att_avg = 100 # reports back as percentage
    # att_sum = 0
    # for i in self.att_entry:
    #   att_sum += int(i.get().strip())
    #   print(att_sum)
    # self.att_avg = str(round(att_sum / len(self.att_entry) * 100, 2))+"%"
    
    # hw_sum = 0
    # for i in self.hw_entry:
    #   hw_sum += int(i.get().strip()) / 100
    # self.hw_avg = str(round(hw_sum / len(self.hw_entry) * 100, 2))+"%"

    # quiz_sum = 0
    # for i in self.quiz_entry:
    #   quiz_sum += int(i.get().strip()) / 100
    # self.quiz_avg = str(round(quiz_sum / len(self.quiz_entry) * 100, 2))+"%"

    # exam_sum = 0
    # for i in self.exam_entry:
    #   exam_sum += int(i.get().strip()) / 100
    # self.exam_avg = str(round(exam_sum / len(self.exam_entry) * 100, 2))+"%"



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
    section_tree = Section_Tree(self, section) 
    add_button = tkinter.Button(self, text='Add Student', command = section_tree.add_student)
    edit_button = tkinter.Button(self, text='Edit Student', command = section_tree.edit_student)

    section_tree.grid(row=0,columnspan=2)
    add_button.grid(row=1, column = 0)
    edit_button.grid(row=1, column=1)
    # tkinter.Label(self, text='Custom frame').grid(row=0)


def new_course():
  New_Course(main_window)

def test_course():
  New_Course(main_window, True)
  


def course_window(course_ID, course_name, attendance_date_template = []):
  def report_size(window):    #debug to report window size for testing
    print(window.winfo_width(), window.winfo_height())
  def report_attendance_range():    #debug to report window size for testing
    for date in attendance_date_template:
      print(date)

  def add_new_section(notebook, course):
    s_frame = Section_Frame(notebook, course.addNewSection())

    text = course.courseID + '-' + "{:02d}".format(course.sectionList[-1].sectionID)
    # notebook.add(child=frame, text=text)
    notebook.add(child=s_frame, text=text)
  
  #generation of the course in question
  #TODO show more than one course in the GUI at the same time
  course = Course(course_ID, course_name, attendance_date_template)
  course.printCourse()

  course_window=tkinter.Toplevel()
  #course_window.geometry('540x400')

  #Menu Bar
  menu_bar = tkinter.Menu(course_window)
  file_menu = tkinter.Menu(menu_bar, tearoff=0)
  file_menu.add_command(label="Save", command=course.writeToFile)
  file_menu.add_separator()
  file_menu.add_command(label="Exit", command=main_window.destroy)
  menu_bar.add_cascade(label="File", menu=file_menu)

  help_menu = tkinter.Menu(menu_bar, tearoff=0)
  help_menu.add_command(label="About", command=lambda: About_Dialog(course_window))    #lamba fixes arguments
  menu_bar.add_cascade(label="Help", menu=help_menu)
  course_window.config(menu=menu_bar)
  

  #window elements with course:
  tkinter.Label(course_window, text = course.courseID + ' - ' + course_name, font=(None, 16)).grid(sticky='W', row=0, column= 0)

  sections_notebook = ttk.Notebook(master=course_window)
  sections_notebook.grid(row=2, columnspan=2, sticky='NS')    # colspan is dirty button spacing fix
  
  #Generate tables from current list
  for section in course.sectionList:
    section_frame = Section_Frame(sections_notebook, section)
    sections_notebook.add(child=section_frame, text=course.courseID + '-' + "{:02d}".format(course.sectionList[-1].sectionID))

  #placing course_window grid
  tkinter.Button(course_window, text="Report size",
                 command=lambda: report_size(course_window)).grid(row=1, column = 0, sticky='W')
  tkinter.Button(course_window, text="Print all dates",
                 command=report_attendance_range).grid(row=3, column = 1, sticky='E')
  add_button = tkinter.Button(course_window, text="Add Section",
                 command=lambda: add_new_section(sections_notebook, course))
  add_button.grid(column=1, row=1, sticky='W')

  tkinter.Button(course_window, text='Print Course',
                 command=course.printCourse).grid(row=3, sticky='w')


main_window = tkinter.Tk()
main_window.title("Class Grader")
#main_window.geometry('400x300')

new_course_button = tkinter.Button(main_window, text="New", state='normal', command=new_course)
test_course_button = tkinter.Button(main_window, text="Test", state='normal', command=test_course)
new_course_button.grid(column=0, row=0)
test_course_button.grid(column=0, row=1)
label = tkinter.Label(main_window, text='Create a new course')
label.grid(column=1, row=0)


# test_button = tkinter.Button(main_window, text="test", state='normal', command=new_course)
# test_button.grid(column=0, row=1)



