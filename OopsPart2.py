### del Keyword
# The del keyword is used to delete objects in Python.
# It can be used to delete variables, list items, dictionary entries, or even entire objects.
# When you use del on an object, it removes the reference to that object, and if there are no other references to it, the object will be garbage collected, freeing up memory.
# del s1.name
# del s1
# del s2


# class Student:
#     def __init__(self, name):
#         self.name = name


# s1 = Student("Sagar Adhikari")
# print(s1.name)

# del s1
# print(s1)  # NameError: name 's1' is not defined


###Private attributes and Methods -> private attributes and methods are ment to be used only within the class and are not accessible from outside the class.
## we use two underscore to make variable private


# class Account:
#     def __init__(self, acc_no, acc_pass):
#         self.__acc = acc_no
#         self.__password = acc_pass

#     def reset_pass(self):
#         print(self.__password) #can access inside class


# acc1 = Account("12345", "abcdef")
# print(acc1.reset_pass())
# print(acc1.__acc)  # error 'Account' object has no attribute '__acc'
# print(acc1.__password)  # this cannot access outside class
