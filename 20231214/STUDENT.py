class student:
    def __init__(self,name,student_ID):
        self.course = []
        self.name = name
        self.student_ID = student_ID
    def student_course(self):
        return self.course
    
    def add_course(self,new_course):
        self.course.extend(new_course)
        
    def withdraw_course(self,del_course):
        if del_course in self.course:
            self.course.remove(del_course)
        else:
            print(f"{del_course}課程並不存在於你選課中")
    def print_data(self):
        print(f"{self.name}目前選到的課程有{self.course}")
def main():
    obj1 = student("huang","4b0g0109")
    obj1.add_course(["test1","test2","test3"])
    obj1.withdraw_course("test2")
    obj1.print_data()
if __name__ == '__main__':
    main()       