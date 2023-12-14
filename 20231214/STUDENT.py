class student:
    def __init__(self,name,student_ID):
        self.course = []
        self._name = name
        self._student_ID = student_ID
    @property
    def student_course(self):
        return self.course
    @student_course.setter
    def add_course(self,new_course):
        self.course.append(new_course)
    @student_course.deleter
    def withdraw_course(self,del_course):
        del self.course[del_course]
    def print_data(self):
        print(f"{self._name}目前選到的課程有{self.course}")
def main():
    obj1 = student("huang","4b0g0109")
    obj1.course = ["test","test2","test3"]
    obj1.course.append("obj3") 
    del obj1.course[1]
    obj1.print_data()
if __name__ == '__main__':
    main()       