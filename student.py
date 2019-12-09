class Student:

    def __init__(self, id, last_name="last_name", first_name = "first_name"):
        print("student constructor")
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        # self.section
        # self.grade = " "  # Grade appears as empty as default
        # Possible that much won't be added here

    def printStudent(self):
        print("Printing Student:  ID:", self.id, "Name:", self.last_name + ",", self.first_name)

