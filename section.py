import student
from grading import Score, Attendance

class Section:

    def student_grade_model(self, id=-1, last_name = 'last_name', first_name = 'first_name'): # id pass to studentID
        return {
            "student": student.Student(id, last_name, first_name),
            "attendances": [],  #Attendance()
            "homeworks": [],         #Score()
            "quizzes": [],           #Score()
            "exams": []              #Score()
        }

    def __init__(self, sectionID=66): #66 is for testing purposes only. should start at 01
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

    def addStudentGrade(self, last_name = "last_name", first_name = "first_name"):
        #adding a student also adds a
        lastStudentGrade = self.student_grade_list[-1]
        newID = lastStudentGrade["student"].student_id+1
        newStudentGrade = self.student_grade_model(newID, last_name, first_name)
        self.student_grade_list.append(newStudentGrade)
        return newStudentGrade



# needs tkinter GUI of table layout
# probably do text version of this database first
