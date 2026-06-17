### POLYMORPHISM - Many + Faces/forms
# means same things can be used in different ways
# Example


#### OPERATOR OVERLOADING && Dunder Functons
print(1 + 2)  # 3
print("sagar" + "Adhikari")  # Concatenate
print([1, 2, 3] + [4, 5, 6])  # merge


# The above case is plus operand with differnet uses used for different forms and the output will also be different.
# this is implicit overloading - the python class already mentioned the first one is adding integer and second one is string concatenate and 3rd one is to merge the list


##Dunder Function -> dunder function proceeded by double underscore _ are dunder function. in p


class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def show_number(self):
        print(self.real, "i +", self.img, "j")

    def __add__(self, num2): #Dunder function with double underscore added
        new_real = self.real + num2.real
        new_img = self.img + num2.img
        return Complex(new_real, new_img)
    
    def __sub__(self, num2): #Dunder function with double underscore added
        new_real = self.real - num2.real
        new_img = self.img - num2.img
        return Complex(new_real, new_img)


c1 = Complex(4, 6)
c1.show_number()

c2 = Complex(3, 4)
c2.show_number()
# if i dont add like this  c3 = c1.add(c2)
#if i want to add like this print(c1 + c2) or c3 = c1 + c2 the dunder function come into action
# without dunder function it throws TypeError: unsupported operand type(s) for +: 'Complex' and 'Complex'
c3 = c1 + c2
c3.show_number()


c4 = c1 - c2
c4.show_number()