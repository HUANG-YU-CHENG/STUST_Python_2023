class Student:
    #類別屬性
    school = "STUST"
    school_addr = "台南市永康區南台街一號"

    def __init__(self,major,student_name,student_ID,Personal_addr,credits,gpa):
        self.major = major
        self.student_name = student_name
        self.student_ID = student_ID
        self.Personal_addr = Personal_addr
        self.credits = credits
        self.gpa = gpa
    def setSchoolName(self,school_name):
        self.school = school_name

    def getSchoolName(self):
        print(self.school)

    def setMajorName(self,major_name):
        self.major = major_name

    def getMajorName(self):
        print(self.major)

    def setSchoolAddr(self, school_addr):
        self.school_addr = school_addr
    
    def getSchoolAddr(self):
        print(self.school_addr)

    def setStudentName(self, student_name):
        self.student_name = student_name

    def getStudentName(self):
        print(self.student_name)

    def setStudentID(self, student_id):
        self.student_id = student_id

    def getStudentID(self):
        print(self.student_id)

    def setPersonalAddr(self, personal_addr):
        self.personal_addr = personal_addr

    def getPersonalAddr(self):
        print(self.personal_addr)

    def setGradePoint(self, credits):
        self.credits = credits

    def getCredits(self):
        print(self.credits)

    def setGPA(self, gpa):
        self.gpa = gpa

    def getGPA(self):
        print(self.gpa)

def main():
    #建立類別為Student的物件Mike
    Mike = Student('CSIE','Mike','4b0g0109','高雄港後',100,6)
    Mike.getSchoolName()
    Mike.getSchoolAddr()
    Mike.getMajorName()
if __name__ == '__main__':
    main()