class employer:#員工類別
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
        print(f"該員工工時有{self.work_time}Hr")
    #計算月薪
    def count_salary(self):
        salary = self.work_time * self.minimum_wage #月薪計算
        print(f"該員工月薪為{salary}元")
    #增加工時
    def add_work_time_hour(self,addtional_work_time):
        print(f"該員工加班時間為{addtional_work_time}Hr,總時{self.work_time + addtional_work_time}Hr")
    #增加年資
    def add_seniority(self,addtional_seniority):
        print(f"該員工額外年資為{addtional_seniority},總年資為{self.seniority + addtional_seniority}")
        
        
class drinks:#飲料類別
    def __init__(self,price,name,sweet):
        self.price = price
        self.name = name
        self.sweet = sweet
    #更換名稱
    def change_name(self,swap_name):
        self.name = swap_name
        print(self.name)
    #調整甜度
    def change_sweet(self,swap_sweet):
        self.sweet = swap_sweet
        print(self.sweet)
    #調整價錢
    def change_price(self,swap_price):
        self.price = swap_price
        print(self.price)
class cold(drinks):#冷飲類別
    def __init__(self,name,ice,sweet,price):
        super().__init__(price,name,sweet)#繼承飲料建構子
        self.name = name
        self.ice = ice
        self.sweet = sweet
        self.price = price
class hot(drinks):#熱飲類別
    def __init__(self,name,sweet,price):
        super().__init__(price,name,sweet)#繼承飲料建構子
        self.name = name
        self.sweet = sweet
        self.price = price
def main():
    Jack = employer("Jack",0.8,120) #員工類別物件
    Jack.check_name()#查詢名字函式
    Jack.check_seniority()#查詢年資函式
    Jack.check_work_time()#查詢工時函式

    Jeff = employer("Jeff",2,130)#員工類別物件
    Jeff.count_salary()#計算月薪函式
    Jeff.add_seniority(1)#增加年資函式

    Jacky = employer("Jacky",0.5,140)#員工類別物件
    Jacky.add_work_time_hour(20)#增加工時函式
    
    obj1 = cold("波霸奶茶","少冰","微糖",60)#冷飲類別物件

    obj2 = cold("綠茶","正常冰","無糖",30)#冷飲類別物件

    obj3 = cold("多多綠","多冰","半糖",35)#冷飲類別物件

    obj4 = hot("黑糖珍珠奶茶","半糖",65)#熱飲類別物件
    
    obj5 = hot("鐵觀音拿鐵","微糖",50)#熱飲類別物件

    obj6 = hot("烏龍茶","半糖",30)#熱飲類別物件
    obj6.change_name("紅茶拿鐵")#更換名稱函式
    obj6.change_sweet("全糖")#調整甜度函式
    obj6.change_price(50)#調整價格
if __name__ == "__main__":
    main()