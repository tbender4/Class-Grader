import student
from grading import Score, Attendance

class Section:

    def __init__(self, sectionID):
        self.sectionID = sectionID
        # self.sectionName = sectionName

        #NEED TO COMBINE THIS
        # self.attendance = Attendance()[]
        # self.homework = Score()[]
        # self.quiz = Score()
        # self.exam = Score()

        self.students = []  # array of students
        #NEED TO COMBINE THIS END

        initialStudent = student.Student(0)
        self.students.append(initialStudent)

    def getSectionID(self):
        return self.sectionID

    def printSection(self):
        print("-----------")
        print("Printing Section: ID:", self.sectionID)
        print("-----------")
        for student in self.students:
            student.printStudent()

    def addStudent(self, last_name = "last_name", first_name = "first_name"):
        newID = self.students[-1].id + 1
        newStudent = student.Student(newID)
        self.students.append(newStudent)


# needs tkinter GUI of table layout
# probably do text version of this database first
