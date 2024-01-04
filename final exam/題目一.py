class fried_chicken:
    def __init__(self,meat,flour,fried_time,flavor,number):
        self.meat = meat
        self.flour = flour
        self.fried_time = fried_time
        self.flavor = flavor
        self.number = number
    def choose_flavor(self):
        return print(self.flavor)
    def prepare_fried_time(self):
        return print(self.fried_time)
    def calling_serving(self):
        return print(self.number)
def main():
    obj1 = fried_chicken("chicken","corn,""vanila","2m30s","a serving")
    obj1.choose_flavor()
    obj1.prepare_fried_time()
    obj1.calling_serving()