class employer:
    def __init__(self,name,seniority,work_time):
        self.name = name
        self.seniority = seniority
        self.work_time = work_time
class drinks:
    def __init__(self,price):
        self.price = price
class cold(drinks):
    def __init__(self,name,ice,sweet):
        self.name = name
        self.ice = ice
        self.sweet = sweet
class hot(drinks):
    def __init__(self,name,sweet):
        self.name = name
        self.sweet = sweet