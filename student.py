class Student:

    def __init__(self, student_id, last_name="last_name", first_name = "first_name"):
        print("student constructor")
        self.first_name = first_name
        self.last_name = last_name
        self.last_first = self.last_name + ', ' + self.first_name
        self.student_id = student_id
        # self.section
        # self.grade = " "  # Grade appears as empty as default
        # Possible that much won't be added here

    def updateLF(self):
        self.last_first = self.last_name + ', ' + self.first_name
    def printStudent(self):
        print("Printing Student:  ID:", self.student_id, "Name:", self.last_name + ",", self.first_name)

    def student_dict(self):
        return {
            "student_id" : self.student_id,
            "first_name" : self.first_name,
            "last_name" : self.last_name,
            "last_first" : self.last_first
        }
