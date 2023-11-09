#Exercise 5: Create an inner function to calculate the addition in the following way
def outer(a,b):
    def add(a,b):
        sum = a + b
        return sum
    result = add(a,b)
    result = result + 5
    return result
print(outer(2,3))