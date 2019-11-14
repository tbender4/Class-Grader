class Student:

    def __init__(self, id, first_name = "first_name", last_name = "last_name"):
        print("constructor")
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        # self.section
        # self.grade = " "  # Grade appears as empty as default
        # Possible that much won't be added here

    def printStudent(self):
        print("-----------")
        print("Printing Student:\n ID:", self.id, "Name:", self.last_name + ",", self.first_name)
        print("-----------")

print("ERROR: Run main.py to run this program")
