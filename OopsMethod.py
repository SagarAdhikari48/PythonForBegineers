### Methods are functions that belongs to objects.
class Student:
    college_name = "ABC"
    
    def __init__(self, name , marks):
        self.name = name
        self.marks = marks
        
    def welcome(self): # Method should always followed with self parameter at first.
        print("Hello Welcome to the pythome programming series learning")
        
    def get_marks(self):
        return self.marks
        
s1 = Student("Sagar Adhikari", 98)
s1.welcome()
s1.get_marks()

print(s1.get_marks())

# Every method we write self