###1. Define a circle class to create a circle with radius r using the constructor.Define an Area() method of hte class which calculates the area of the circle.Define a perimeter() method of the class which allow to calculate the perimeter of circle.


# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def calculate_area(self):
#         self.area = (22 / 7) * self.radius**2
#         return self.area

#     def perimeter(self):
#         return 2 * (22 / 7) * self.radius


# c1 = Circle(21)
# area = c1.calculate_area()
# print(area)


# perimeter = c1.perimeter()
# print(perimeter)


###2. Define a Employe class with attr role, department and salary. this class should have showDetails() method. Create engineer class that inherits properties from employee and
# has additional attributes name and age.


class Employee:
    def __init__(self, department, role, salary):
        self.role = role
        self.department = department
        self.salary = salary

    def show_details(self):
        print("your department is : ", self.department)
        print("your role is : ", self.role)
        print("your salary is : ", self.salary)


class Engineer(Employee):
    def __init__(self, age, name):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", "6000000")


# emp = Employee("It", "Software Developer", 3000)
# emp.show_details()

eng1 = Engineer("Elon Musk", 50)
eng1.show_details()


#### 3. Create a class called Order which stores item and price. Use Dunder function __gt__() to convey that
# order1 > order2 if the price of Order1 > price of order2


class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price
        
    def __gt__(self, od2):
        return self.price > od2.price


od1 = Order("Pizza", 250)
od2 = Order("Samosa", 200)

print(od1 > od2)
