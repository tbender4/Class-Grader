import tkinter


def aboutMenu():
  description ="""Class Grader is a college Python project
demonstrating I/O, classes, data structures, matplotlib, and tkinter.

Author: Thomas Bender
Contact: tbender4@gmail.com

This software is open source and is hosted on github.com/tbender4/Class-Grader"""

  about = tkinter.Toplevel()
  about.title("Class Grader")

  msg = tkinter.Message(about, text = description)
  msg.pack()
  tkinter.Button(about, text="Close", command=about.destroy).pack()

  about.geometry('220x200')
  about.grab_set()
  about.mainloop()



def course_window():
  course_window=tkinter.Tk()

  menu_bar = tkinter.Menu(course_window)
  file_menu = tkinter.Menu(menu_bar, tearoff=0)
  menu_bar.add_cascade(label="File", menu=file_menu)

  help_menu = tkinter.Menu(menu_bar, tearoff=0)
  help_menu.add_command(label="About", command=aboutMenu)
  menu_bar.add_cascade(label="Help", menu=help_menu)
  

  course_window.config(menu=menu_bar)
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

