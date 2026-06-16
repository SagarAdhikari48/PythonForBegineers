### Abstraction -> Hiding the implementation details of a class and only showing the essential features to the users.
### Encapsulation -> Wrapping data and functions into a single unit(object).

class Car:
    def __int__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
        
    def start(self):
        self.clutch = True
        self.acc = True
        print("The car started!")
c1 = Car()
c1.start()



### so in the above case the details of clutch and acc are not displayed to user called Abstraction and whole program unit called Encapsulation