###1. Define a circle class to create a circle with radius r using the constructor.Define an Area() method of hte class which calculates the area of the circle.Define a perimeter() method of the class which allow to calculate the perimeter of circle.


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        self.area = (22 / 7) * self.radius**2
        return self.area

    def perimeter(self):
        return 2 * (22 / 7) * self.radius


c1 = Circle(21)
area = c1.calculate_area()
print(area)


perimeter = c1.perimeter()
print(perimeter)
