# import grading
import json
import section
import os


class Course:

    __keys  = [ "courseID", "name", "sectionList"]

    def __init__(self, courseID, name = "", attendance_date_template = ['00/00/00']):
        self.name = name
        if name == "":
            self.name = courseID    #Copies text of courseID
        self.courseID = courseID
        initialSection = section.Section(1)
        self.sectionList = []
        self.attendance_date_template = attendance_date_template
        self.sectionList.append(initialSection)

    def writeToFile(self):
        localdir = os.path.dirname(__file__)
        datapath = os.path.join(localdir, 'saved', '{}.json'.format(self.courseID))
        
        sections = {}
        for s in self.sectionList:
            sections.update(s.section_dict())
        # sections = [s.section_dict() for s in self.sectionList]
        course_dict = {
            "courseID" : self.courseID,
            "name" : self.name,
            "sectionList" : sections
        }
        with open(datapath, 'w') as json_file:
            json.dump(course_dict, json_file, indent=2)


    def addNewSection(self):
        newSection = section.Section((self.sectionList[-1].sectionID)+1) #quick generation of ID
        self.sectionList.append(newSection)
        return self.sectionList[-1] #returns back added section for use in GUI
    
    # edit 

    def printCourse(self):
        print("Printing Course:", self.courseID, " Name:", self.name)
        for section in self.sectionList:
            section.printSection()