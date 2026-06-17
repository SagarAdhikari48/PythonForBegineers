### Methods are functions that belongs to objects.
# class Student:
#     college_name = "ABC"
    
#     def __init__(self, name , marks):
#         self.name = name
#         self.marks = marks
        
#     def welcome(self): # Method should always followed with self parameter at first.
#         print("Hello Welcome to the pythome programming series learning")
        
#     def get_marks(self):
#         return self.marks
        
# s1 = Student("Sagar Adhikari", 98)
# s1.welcome()
# s1.get_marks()

# print(s1.get_marks())

# Every method we write self



###1. Create student class that takes name and marks of three subjects as arguments in constructor. Then create a method to print average.

class Student:
    average = 0
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        

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


