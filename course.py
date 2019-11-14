# import grading
import section

class Course:
    def __init__(self, courseID, name):
        self.name = name
        self.courseID = courseID
        initialSection = section.Section(0)
        self.sectionList = []   #creates one initial section.
        self.sectionList.append(initialSection)


    def addNewSection(self):
        newSection = section.Section(self.sectionList[-1].getSectionID()+1)
        self.sectionList.append(newSection)
    
    # delete section

    def printCourse(self):
        print("Printing Course:", self.courseID, " Name:", self.name)
        for section in self.sectionList:
            section.printSection()
