# loops are used to repeat instructions.
# In python - while loop and for loop

# 1. WHILE LOOP
# Syntax
# while condition:
# some work

# while True:  #-> this prints infinitely!
#     print("Hello Sagar")

# count = 1.0  # iterator
# while count <= 5:
#     print("Hello Sagar")
#     count += 1

# print(count)  # 6


# i = 1
# while i <= 100000:
#     print("Hello", i)
#     i += 1


# i = 1
# while i <= 5:
#     print(i)
#     i += 1
# print("Loope ended!")

# Print numbers from 5 to 1

# i = 5
# while i >= 1:
#     print(i)
#     i -= 1

# print("loops ended!")


### 1. Print numbers from 1 to 100.
# i = 1
# while i <= 100:
#     print(i)
#     i += 1
# print("Printed from 1 to 100")

### 2. print numbers from 100 to 1
# i = 100
# while i >= 1:
#     print(i)
#     i -= 1
# print("Printed from 100 to 1")

### 3. Print the multiplication of table of number n.

# factor = 1
# number = int(input("enter the number"))
# while factor <= 10:
#     mul = number * factor
#     factor += 1
#     print("the multiplication is ", mul)

### 4. Print the elements of the following list using a loop
# [1, 4,9, 16, 25, 36, 49, 64, 81, 100]

# num = 1
# array = []
# while num <= 10:
#     square = num**2
#     array.append(square)
#     num += 1
#     print("square is :", square)

#     print(array)

#     ###ORED print-elemets only
#     nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#     idx = 0
#     while idx < len(nums):
#         print(nums[idx])
#         idx += 1


### 5. Search for X number in this tuple using loop
# (1, 4, 9, 16, 25, 36,49,64,81,100)
# i = 0
# nums = (1, 4, 9, 16, 25, 36,49,64,81,100 ,9 , 16)
# print("Question 5 tuples length: ",len(nums))
# search = int(input("Enter the number you want to find : "))
# while i < len(nums) :
#     if(search == nums[i]):
#         print("Searched number is found as at index  : ", nums[i],"at index", i)
#         break
#     else:
#         print("Finding...")

#     i += 1

# print("End!")

### BREAK AND CONTINUE
# Break - Used to terminate the loop when encountered.

# i =1
# while i <= 5:
#     print(i)
#     if(i == 3):
#         break;
#     i += 1


### Continue - the condition will skip by the continue statement- below the 3 will not printed because it skips that condition as
# 0
# 1
# 2
# 4
# 5
# - Used to skip the current iteration and move to next one.
# - Terminates execution in the current iteration and continues execution of the loop with the next iteration

# i = 0
# while i <= 5:
#     if i == 3:
#         i += 1
#         continue  # skip 3
#     print(i)
#     i += 1

# print odd number between 1 - 10

# i = 1
# while i <= 10:
#     if i % 2 == 0: #skips the even number i.e number divided by 2 will be skipped
#         i += 1
#         continue
#     print(i)
#     i += 1


# print even number between 1 - 10

# i = 1
# while i <= 10:
#     if(i % 2 != 0) : #skips the odd number i.e number divided by 2 will be skipped
#         i += 1
#         continue
#     print(i)
#     i += 1


### FOR LOOPS - For loops are used for the sequential traversal. For traversing list, string, tuples etc
# list = [1, 4, 9, 16, 25, 36,49,64,81,100]

# for num in list:
#     print(num)


# veggies = ["potato", "onion", "cabbage", "brinjal", "ladyfinger"]
# for veg in veggies :
#     print(veg)


### For loops in Tuples

# tup = (1, 2, 3, 4, 5, 2, 8, 9)
# for val in tup:
#     print(val)


### FOr loop in strings
# str = "My name is sagar"
# for ch in str:
#     print(ch)


### Else case in for loop - when ever we break the statement we need else case

# string = "Sagaradhikari"
# for ch in string:
#     if(ch == "d"):
#         print("character d is found!")
#         break
#     print(ch)
# else:
#     print("End")


### 1. Print the elements of the following list using a for loop
# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# for num in nums:
#     print(num)

### 2. Search for a number X in this tuple using for loop

# numberToSearch = int(input("Enter the number to be searched!"))
# tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 9, 16, 49, 81, 25)
# idx = 0
# for num in tup:
#     if num == numberToSearch:
#         print("the searched number is ", num, "at index ", idx)
#         # break
#     idx += 1


# else:
#     print("EOF")


### Range Function -
# return the sequence of numbers always starting from 0 by default and increments by 1 default
# and stop before a specified number.
## range(start?, stop, step?)


# seq = range(5)
# for el in seq:
#     print(el)


# for i in range(10): # range(stop condition)
#     print(i)


# for i in range(2,10): #range (start, stop)
#     print(i)


# for i in range(2,10,2): #range (start, stop, step)
#     print(i)


###1. print all even number
# for i in range(2, 100, 2):
#     print(i)


# 1.Print number 1 to 100 using for and range method
# for i in range(1, 101):
#     print(i)
# # 2.Print number 100 to 1 using for and range method
# for i in range(100, 0, -1):
#     print(i)
# # # 1.printing multiplication table
# number = int(input("enter the number"))
# for i in range( 1, 11):
#     print(number * i)


### Pass Statement -> Pass statement is a null statement that does nothing . It is used as a placeholder for future code.

# for i in range(5):
#     pass  # not weiting code here now but in future we might add
# print("somethind is done")


# # Practice Questions:
# # 1. Write the program to add sum of n natural number
# n = int(input("enter the number to sum"))
# sum = 0
# for i in range(1, n + 1):
#     sum += i

# print(sum)


# 2.  WAP to find factorial of n number - using for loop
# n = int(input("Enter the number to find the factorial"))
# fact = 1
# i = 1
# while i <= n:
#     fact *= i
#     i += 1

# print(fact)


n = int(input("Enter the number to find the factorial"))
fact = 1
for i in range(1, n + 1):
    fact *= i
print(fact)
