### del Keyword
# The del keyword is used to delete objects in Python. 
# It can be used to delete variables, list items, dictionary entries, or even entire objects. 
# When you use del on an object, it removes the reference to that object, and if there are no other references to it, the object will be garbage collected, freeing up memory.
# del s1.name
# del s1
# del s2

class Student:
    def __init__(self, name):
        self.name = name
        
s1 = Student("Sagar Adhikari")
print(s1.name)

del s1
print(s1) #NameError: name 's1' is not defined
