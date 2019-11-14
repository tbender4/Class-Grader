import student

class Section:
    def __init__(self, sectionID):
        self.sectionID = sectionID
        # self.sectionName = sectionName
        self.attendance = []
        self.homework = []
        self.quiz = []
        self.exam = []

        self.students = []  # array of students
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
