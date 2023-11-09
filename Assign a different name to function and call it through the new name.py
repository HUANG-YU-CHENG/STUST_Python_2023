#Exercise 7:Assign a different name to function and call it through the new name
def display_student(name, age):
    print(name, age)

display_student("Emma", 26)

# assign new name
showStudent = display_student
# call using new name
showStudent("Emma", 26)