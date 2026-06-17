# Class attributes defines only once in a memory
class Student:
    college_name = "Advanced College" # This is a class attributes - the s1 and s2  object should have same college name.
    name = "any" # class attributes
    def __init__(self, fullname, marks):
        self.name = fullname  # Object attr > class attr so the print(s1.name will print "Sagar Adhikari" not "any " in the class)
        print("Adding new student in database...")


s1 = Student("Sagar Adhikari", 80)
print(s1.name, s1.marks)


s2 = Student("Aarogy Adhikari", 90)
print(s2.name, s2.marks)
print(s2.college_name)
# also 
print(Student.college_name)
