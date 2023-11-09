#Exercise 2: Create a function with variable length of arguments
def func1(*val):
    for i in val:
        print(i)
func1(20,30)