#Exercise 6: Create a recursive function
def recursive(num):
    if num:
        return num + recursive(num - 1)
    else:
        return 0
res = recursive(10)
print(res)