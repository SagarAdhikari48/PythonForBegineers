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


####1. Create Account class with 2 attributes - balance and account no. Create methods for debit, credit and  printing the balance.

class Account:
     def __init__(self, blc ,acc_no):
         self.balance = blc
         self.account_number = acc_no
         print("hi your account", acc_no, "has ", blc)
         
     def debit(self, amount):
         self.balance -= amount
         print("Rs", amount, "was debited")
         print("Total balance = ", self.get_balance())
         
     def credit(self, amount):
         self.balance += amount
         print("Rs", amount, "was credited")
         print("Total balance = ", self.get_balance())
         
         
     def get_balance(self):
         return self.balance
        
         
        
         
a1 = Account(350, 12344232)
a1.debit(30);
a1.credit(50);
a1.get_balance()

