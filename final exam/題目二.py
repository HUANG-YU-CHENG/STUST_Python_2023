class employer:
    def __init__(self,name,seniority,work_time):
        self.minimum_wage = 173 #基本時新
        self.name = name
        self.seniority = seniority
        self.work_time = work_time
    #查詢名字
    def check_name(self):
        print(f"員工名為{self.name}")
    #查詢年資
    def check_seniority(self):
        print(f"該員工年薪有{self.seniority}")
    #查詢工時
    def check_work_time(self):
        print(f"該員工工時有{self.work_time}")
    #計算月薪
    def count_salary(self):
        salary = self.work_time * self.minimum_wage #月薪計算
        print(f"該員工月薪為{salary}")
    #增加工時
    def add_work_time_hour(self,addtional_work_time):
        print(f"該員工加班時間為{addtional_work_time},總時{self.work_time + addtional_work_time}")
    #增加年資
    def add_seniority(self,addtional_seniority):
        print(f"該員工額外年資為{addtional_seniority},總年資為{self.seniority + addtional_seniority}")
        
        
class drinks:
    def __init__(self,price,name,sweet):
        self.price = price
        self.name = name
        self.sweet = sweet
    #更換名稱
    def change_name(self,swap_name):
        self.name == swap_name
        print(self.name)
    #調整甜度
    def change_sweet(self,swap_sweet):
        self.sweet == swap_sweet
        print(self.sweet)
    #調整價錢
    def change_price(self,swap_price):
        self.price == swap_price
        print(self.price)
class cold(drinks):
    def __init__(self,name,ice,sweet):
        super().__init__(self.price)
        self.name = name
        self.ice = ice
        self.sweet = sweet
class hot(drinks):
    def __init__(self,name,sweet):
        self.name = name
        self.sweet = sweet
def main():
    Jack = employer("Jack",0.8,120)
    Jack.check_name()
    Jack.check_seniority()
    Jack.check_work_time()
    Jeff = employer("Jeff",2,130)
    Jeff.count_salary()
    Jeff.add_seniority(1)
    Jacky = employer("Jacky",0.5,140)
    Jacky.add_work_time_hour(20)
if __name__ == "__main__":
    main()