# Static methods are the methods they dont use the self parameters
# @staticmethod decorators are used to define static method 

# class Student:
#     @staticmethod
#     def college():
#         print("This is my college:")
        
###Example
class Student:
    average = 0
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
        
    @staticmethod # this fixes the error otherwise self parameter required
    def hello():
        print("Hello!")
        

    def calculate_average(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi ", self.name, "your score is : ",sum / 3)
        return sum / 3
        

s1 = Student("Sagar", [99, 98, 97])
s1.calculate_average()

s1.name = "Adhikari"
s1.calculate_average()

s1.hello() # this will throw error as : Student.hello() takes 0 positional arguments but 1 was given if no static method decorator is added