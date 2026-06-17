### Inheritance -> When one class (child/derived). derives the properties and methods of another class(parent/base).
# to show inheritance we use parenthesis in child class and take argument  of parent class name in the child class.
## Properties -> Attributes and Methods
# Syntax

# class Car:
#     .......

# class ToyataCar(Car):
#     .........

# class Car:
#     color = "black"
#     @staticmethod
#     def start():
#         print("Car started...")

#     @staticmethod
#     def stop():
#         print("The car stopped...")

# class ToyataCar(Car):#Inheritance
#     def __init__(self, name):
#         self.name = name

# car1 = ToyataCar("fortuner")
# car2 = ToyataCar("prius")

# print(car1.name)
# print(car2.name)

# print(car1.start()) #this is due  inheritance
# print(car1.color) ## attributes inherit


### Multilevel inheritance -> Inheritance goes level wise

# class Car:
#     @staticmethod
#     def start():
#         print("Car started...")

#     @staticmethod
#     def stop():
#         print("The car stopped...")

# class ToyataCar(Car):#Inheritance
#     def __init__(self, brand):
#         self.brand = brand

# class Fortuner(ToyataCar):
#     def __init__(self, type):
#         self.type = type

# car1 = Fortuner("Diesel")
# car1.start()


### MULTIPLE INHERITANCE - A child class inherit multiple parent class
# class A:
#     varA = "Welcome to class A"

# class B:
#     varB = "Welcome to class B"

# class C(A, B):
#     varC = "Welcome to class C"

# c1 = C()
# print(c1.varA)
# print(c1.varB)
# print(c1.varC)

####SUPER METHOD -> whenever we need to call any method in parent class we need to use super


class Car:

    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("Car started...")

    @staticmethod
    def stop():
        print("The car stopped...")


class ToyataCar(Car):  # Inheritance
    def __init__(self, name, type):
        super().__init__(type) # this will pass type to parent class and will not throw wrror
        self.name = name
        super().start()

car1 = ToyataCar("pirus", "electric")
print(car1.type)
