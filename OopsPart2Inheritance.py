### Inheritance -> When one class (child/derived). derives the properties and methods of another class(parent/base).
# to show inheritance we use parenthesis in child class and take argument  of parent class name in the child class.
## Properties -> Attributes and Methods
#Syntax
 
# class Car:
#     .......
    
# class ToyataCar(Car):
#     .........

class Car:
    color = "black"
    @staticmethod
    def start():
        print("Car started...")
        
    @staticmethod
    def stop():
        print("The car stopped...")
        
class ToyataCar(Car):#Inheritance 
    def __init__(self, name):
        self.name = name
        
car1 = ToyataCar("fortuner")
car2 = ToyataCar("prius")

print(car1.name)
print(car2.name)

print(car1.start()) #this is due  inheritance
print(car1.color) ## attributes inherit
        