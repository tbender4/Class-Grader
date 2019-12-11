# import grading
import section

class Course:
    def __init__(self, courseID, name = ""):
        self.name = name
        if name == "":
            self.name = courseID    #Copies text of courseID
        self.courseID = courseID
        initialSection = section.Section(1)
        self.sectionList = []
        self.sectionList.append(initialSection)


    def addNewSection(self):
        newSection = section.Section(self.sectionList[-1].getSectionID()+1) #quick generation of ID
        self.sectionList.append(newSection)
        return self.sectionList[-1] #returns back added section for use in GUI
    
    # edit 

    def printCourse(self):
        print("Printing Course:", self.courseID, " Name:", self.name)
        for section in self.sectionList:
            section.printSection()