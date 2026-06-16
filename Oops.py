### CLass and Objects in Python
# - Class is a blueprint for creating objects- objects cannot create without class


# Creating Class
# class Student:
#     name = "Sagar Adhikari"


# # Creating Object (instance)

# s1 = Student()  # new object of class
# print(s1.name)

# s2 = Student()
# print(s2.name)


# class Car: # THis is how class is created 
#     color = "red"
#     brand = "BYD"
    
# car1 = Car() # This is how the objects were created!
# print(car1.color)
# print(car1.brand)



### CONSTRUCTOR - are also called __init__ function - Invoked at the time of object creation -  invoked meand executed
# All classes have a function called _init_(), which is always executed when the object is being initialized.
#Example

class Student:
    name = "Sagar Adhikari"

s1 = Student()
print(s1.name)

s2 = Student()
print(s2.name)
#Here no init function is defined but it automatically creates the init function and executed. there will be always condtructure for us.
