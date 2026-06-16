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
# Example


class Student:

    # DEfault Constructor
    def __init__(self):
        print("this is. a default constructor")

        ## Parameterized Constructor
    def __init__(
        self, fullname, marks
    ):  ## Self refers to the new object beiing created. self means my self
        # print(self) #This will prints <__main__.Student object at 0x1007e8550> student object at that location 0x100....
        self.name = fullname
        self.marks = marks
        print(
            "Adding new student in database..."
        )  # this constructor invoked automatically


s1 = Student("Sagar Adhikari", 80)
# print("this means constructor self simply mean  self means s1 object",s1)
print(s1.name, s1.marks)


s2 = Student("Aarogy Adhikari", 90)
print(s2.name, s2.marks)


##Output
# Adding new student in database...
# Sagar Adhikari
# Adding new student in database...
# Aarogy Adhikari

## THe self parameter in the constructor above is a reference to the current instance of the class and is used to access variables that belongs to the class.
# With the help of the self parameter we can store different variables or different datas.
# THe data stored inside class or the object are called attributes or variables.
# We will not define multiple constructor for a single class
