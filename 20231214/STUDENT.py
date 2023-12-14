class student:
    def __init__(self,name,student_ID):
        session = []
        self.session = session
        self._name = name
        self._student_ID = student_ID
    @property
    def student_session(self):
        return self.session
    @student_session.setter
    def add_session(self,new_session):
        self.session.append(new_session)
    @student_session.deleter
    def withdraw_session(self,del_session):
        del self.session[del_session]
    def print_data(self):
        print(f"{self._name}目前選到的課程有{self.session}")
def main():
    obj1 = student("huang","4b0g0109")
    obj1.session = ["test","test2","test3"]
    obj1.session.append("obj3") 
    del obj1.session[1]
    obj1.print_data()
if __name__ == '__main__':
    main()       