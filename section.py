import student
import datetime
from grading import Score, Attendance


class Section:
    
    def student_grade_model(self, id=-1, last_name = 'last_name', first_name = 'first_name', attendances = [Attendance()]): # id pass to studentID
        return {
            "student": student.Student(id, last_name, first_name),
            "attendances": attendances,  #Attendance()
            "homeworks": [],         #Score()
            "quizzes": [],           #Score()
            "exams": []              #Score()
        }

    def __init__(self, sectionID=66): #66 is for testing purposes only. should start at 01
        self.sectionID = sectionID
        self.attendance_dates = []      #Generating attendances per student should be copied from here
                                        #so each student is consistent
                                        #list of Attendances.
        self.student_grade_list = []  # array of students and their grades

        self.student_grade_list.append(self.student_grade_model(id=0, attendances=self.attendance_dates))
        
    def add_attendance_date(self, date_string = None):
        #adds to the global attendance_dates.
        #TODO: Add code that'll replace in the student info
        if not date_string:
            #if info not given, default to today's date
            self.attendance_dates.append(Attendance())
        else:
            # using american date system for now.
            date = datetime.datetime.strptime(date_string, '%m/%d/%y')
            self.attendance_dates.append(Attendance(date=date))
            #date will be of type string. Parse before sending it to attendance

    def update_all_attendance(self):
        #if student has that attendance, do nothing. Otherwise continue on the other way
        #TODO: This is O(n^2). Needs proper search algorithm.
        for student_grade in student_grade_list:
            for attendance in student_grade['attendances']:
                pass
    #TODO: Make attendnace dictionary of { date: status } Then redo this function   

    def section_dict(self): #returns itself as dict format
        students = []
        for student_grade in self.student_grade_list:
            
            attendances = [attendance.day_status for attendance in student_grade["attendances"]]
            homeworks = [homework.score_dict() for homework in student_grade["homeworks"]]
            quizzes = [quiz.score_dict() for quiz in student_grade["quizzes"]]
            exams = [exam.score_dict() for exam in student_grade["exams"]]
            #converts all to safe formats for json

            students.append( {
                "student" : student_grade.get("student").student_dict(),
                "attendances":student_grade["attendances"],
                "homeworks":student_grade["homeworks"],
                "quizzes":student_grade["quizzes"],
                "exams":student_grade["exams"],
                # TODO: Need to write dict output functions for Score, Attendances
                }
            )
        return {
            self.sectionID : students
        }



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
            print('\nExams:', end='')
            for exam in student_grade["exams"]:
                exam.printScore()
                print(', ', end='')
            print()
        print("\n-----------")

    def addStudentGrade(self, last_name = "last_name", first_name = "first_name"):
        lastStudentGrade = self.student_grade_list[-1]
        newID = lastStudentGrade["student"].student_id+1
        newStudentGrade = self.student_grade_model(newID, last_name, first_name)

        self.student_grade_list.append(newStudentGrade)
        return newStudentGrade

    def editStudentGrade(self, **kwargs):
        
        return




# needs tkinter GUI of table layout
# probably do text version of this database first
