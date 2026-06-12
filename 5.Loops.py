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

i = 1
while i <= 10:
    if(i % 2 != 0) : #skips the odd number i.e number divided by 2 will be skipped 
        i += 1
        continue
    print(i)
    i += 1
