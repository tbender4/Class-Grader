# Class-Grader

A class-grading program written in Python using tkinter GUI.

## Motivation

This is my most cohesive self-driven programming project in college. The idea of this program is to use OOP principles and challenge myself to make a coherent project.

Class-Grader is a rolling development.

## A word on tkinter

While tkinter and traditional GUI applications have fallen out of favor with the rise of web apps and their frameworks, sticking with a traditional GUI experience is a personal choice as I felt it's sufficient enough for this type of software. The footprint is rather small and the usability so far has kept up. I've attempted to write functions in classes outside of the GUI class so it can be ported to perhaps a web app or even a different GUI library. Tkinter's a bit frustrating with scattered online documentation but reading the original source and its comments has been a great help.

## Screenshots

The functionality of this software is best explained in screenshots of it current state in development.

![Cap 1](https://github.com/tbender4/Class-Grader/raw/dev/screencaps/cap1.png)
![Cap 2](https://github.com/tbender4/Class-Grader/raw/dev/screencaps/cap2.png)
![Cap 3](https://github.com/tbender4/Class-Grader/raw/dev/screencaps/cap3.png)

## Ideas

06/08:
Treeview `focus()` is just the last selected. `selection()` is what I need to allow multiple selection. Make this changes after current app works.

06/07:

- [ ] Complete the remaining parts of the student_grade dictionary
- [ ] Finish Attendance GUI so it can editable
- [ ] Score needs to be editable. Then implement in GUI
- [ ] Score needs to be expandable yet reflecting for every student.
- [ ] Once basic editable works, implement useful functions for switching scores, status of attendance, etc
- [ ] Improve UI size
- [ ] Continue implemention of file I/O
- [ ] implement calculation of grades. Toggling curve and not
- [ ] Bell curve with matplotlib.
