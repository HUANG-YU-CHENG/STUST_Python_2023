

class Myclass:
    x = 5
    def __init__(self) ->  None:
        pass

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
 
  def __str__(self):
    return f"Name: {self.name}\nAge = {self.age}"

import math

class Myshape:
    def __init__(self,square_side,width,length,radius):
        self.square_side = square_side
        self.width = width
        self.length = length
        self.radius = radius
    def Count_Square(self):
        return f"Square = {self.square_side * self.square_side}"
    def Count_retangle(self):
        return f"Retangle = {self.width * self.length}"
    def Count_circle(self):
        return f"Circle = {self.radius * self.radius * math.pi}"
def main():
    p1 = Person("John", 36)
    print(p1)
    value = Myshape(5,4,3,3)
    print(value.Count_Square())
    print(value.Count_retangle())
    print(value.Count_circle())
if __name__ == '__main__':
    main()