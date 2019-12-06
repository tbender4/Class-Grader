import tkinter

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


def course_window():
  course_window=tkinter.Toplevel()

  menu_bar = tkinter.Menu(course_window)
  file_menu = tkinter.Menu(menu_bar, tearoff=0)
  menu_bar.add_cascade(label="File", menu=file_menu)

  help_menu = tkinter.Menu(menu_bar, tearoff=0)
  help_menu.add_command(label="About", command=lambda: About_Modal(course_window))    #lamba fixes arguments
  menu_bar.add_cascade(label="Help", menu=help_menu)
  

  course_window.config(menu=menu_bar)
  
  main_window.withdraw()
  course_window.mainloop()

  

def new_course():
  course_init_prompt = tkinter.Tk()
  course_init_prompt.title("Enter New Course")

  courseID_label = tkinter.Label(course_init_prompt, text="Course ID:")
  courseID_entry = tkinter.Entry(course_init_prompt)
  


main_window = tkinter.Tk()
main_window.title("Class Grader")

main_window.geometry('400x300')


new_course_button = tkinter.Button(main_window, text="New", state='normal', command=course_window)
new_course_button.grid(column=0, row=0)
label = tkinter.Label(main_window, text='Create a new course')
label.grid(column=1, row=0)

