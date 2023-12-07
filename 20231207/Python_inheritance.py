#定義sport類別
class Sports:
    def __init__(self,name):
        self._name = name
    #封裝name資料
    @property
    def sports_name(self):
        return self._name
    #更新sport_name資料
    @sports_name.setter
    def sports_name(self,value):
        self._name = value
class LandSports(Sports):
    def __init__(self,name,field):
        super().__init__(name)
        self._field = field
    #封裝field資料
    @property
    def landsports_field(self):
        return self._field
    #更新field資料
    @landsports_field.setter
    def landsports_field(self,value):
        self._field = value
class WaterSport(Sports):
    def __init__(self,name,activities):
        super().__init__(name)
        self._activities = activities
    #封裝activities資料
    @property
    def watersports_activities(self):
        print(f'"{self._name}"在{self._activities}運動.')
        return self._activities
    #更新activities資料
    @watersports_activities.setter
    def watersports_activites(self,value):
        self._activities = value 
def main():
    #創建LandSport物件
    soccer = LandSports("soccer","ball")
    print(soccer.sports_name)
    print(soccer.landsports_field)
    #創建WaterSport物件
    artistic_swimming = WaterSport("artistic swimming","swimming pool")
    print(artistic_swimming.sports_name)
    print(artistic_swimming.watersports_activities)
if __name__ == '__main__':
    main()