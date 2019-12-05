import student
from grading import Score, Attendance

class Section:

    def student_grade_model(self, id=-1): # id pass to studentID
        return {
            "student": student.Student(id),
            "attendances": [],  #Attendance()
            "homeworks": [],         #Score()
            "quizzes": [],           #Score()
            "exams": []              #Score()
        }

    def __init__(self, sectionID):
        self.sectionID = sectionID

        self.student_grade_list = []  # array of students
        self.student_grade_list.append(self.student_grade_model(0))
        


    def getSectionID(self):
        return self.sectionID

    def printSection(self):
        print("-----------")
        print("Printing Section: ID:", self.sectionID)
        for student_grade in self.student_grade_list:
            student_grade["student"].printStudent()
            print("Attendances:",end='')
            for attendance in student_grade["attendances"]:
                attendance.printAttendance()
                print(', ', end='')
            print('\nHomeworks: ', end='')
            for homework in student_grade["homeworks"]:
                homework.printScore()
                print(', ', end='')
            print('\nQuiz: ', end='')
            for quiz in student_grade["quizzes"]:
                quiz.printScore()
                print(', ', end='')
            print('\nExams: ', end='')
            for exam in student_grade["exams"]:
                exam.printScore()
                print(', ', end='')
        print("\n-----------")

    def addStudent(self, last_name = "last_name", first_name = "first_name"):
        #adding a student also adds a
        lastStudent = self.student_grade_list[-1]
        newID = lastStudent["student"].id
        newStudent = self.student_grade_model(newID)
        self.student_grade_list.append(newStudent)



# needs tkinter GUI of table layout
# probably do text version of this database first
