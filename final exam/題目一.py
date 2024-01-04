class fried_chicken:
    def __init__(self,meat,flour,fried_time,flavor,number):#建構子分別為肉的種類 麵粉選擇 油炸時間 口味 份量
        self.meat = meat
        self.flour = flour
        self.fried_time = fried_time
        self.flavor = flavor
        self.number = number
    #選擇口味
    def choose_flavor(self):
        print(f"你選擇的口味是{self.flavor}口味")
    #準備時間
    def prepare_fried_time(self):
        print(f"準備時間需要{self.fried_time}")
    #選擇份量
    def calling_serving(self):
        print(f"選擇份量為{self.number}")
def main():
    obj1 = fried_chicken("雞胸肉","玉米粉","2m30s","香草","一份")
    obj1.choose_flavor()
    obj1.prepare_fried_time()
    obj1.calling_serving()

    obj2 = fried_chicken("烏骨雞","麵粉","3m30s","黑胡椒","三份")
    obj2.choose_flavor()
    obj2.prepare_fried_time()
    obj2.calling_serving()

    obj3 = fried_chicken("雞腿","玉薯粉","2m00s","韓式炸雞","兩份")
    obj3.choose_flavor()
    obj3.prepare_fried_time()
    obj3.calling_serving()

    obj4 = fried_chicken("雞胸肉","麵粉","3m00s","黑胡椒","九份")
    obj4.choose_flavor()
    obj4.prepare_fried_time()
    obj4.calling_serving()
if __name__ == '__main__':
    main()