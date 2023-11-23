class Employee():
    def __init__(self,emp_id,emp_name,emp_salary,emp_department):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.emp_salary = emp_salary
        self.emp_department = emp_department
    #調動員工部門函數
    def assign_department(self,name,sector):
        self.sector = sector
        self.name = name
        print(self.name + " change assign department to " + self.sector)
    #列印員工資訊函數
    def print_employee_details(self):
        print(self.emp_id,self.emp_name,self.emp_salary,self.emp_department)
    #計算薪水函數
    def calculate_emp_salary(self,salary,hour_worked):
        self.salary = salary
        self.hour_worked = hour_worked
        if(self.hour_worked > 50):#計算加班費
            overtime = self.hour_worked - 50
            Overtime_amount = (overtime * (self.salary / 50))
            print("This month total amount is " + str(Overtime_amount + self.salary))
        else:
            print("This month total amount is " + str(self.salary))
def main():
    emp1 = Employee("ADAMS", "E7876", 50000, "ACCOUNTING")
    emp2 = Employee("JONES", "E7499", 45000, "RESEARCH")
    emp3 = Employee("MARTIN", "E7900", 50000, "SALES")
    emp4 = Employee("SMITH", "E7698", 55000, "OPERATIONS")
    print("Original Employee Details: ")
    emp1.print_employee_details()
    emp2.print_employee_details()
    emp3.print_employee_details()
    emp4.print_employee_details()
    print("Change assign department: ")
    emp1.assign_department(emp1.emp_id,"SALES")
    emp3.assign_department(emp2.emp_id,"ACCOUNTING")
    print("Calculate Employee salary: ")
    emp1.calculate_emp_salary(emp1.emp_salary,60)
    emp2.calculate_emp_salary(emp2.emp_salary,50)
    emp3.calculate_emp_salary(emp3.emp_salary,70)
    emp4.calculate_emp_salary(emp4.emp_salary,55)
if __name__ == '__main__':
    main()