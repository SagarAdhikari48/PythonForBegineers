# loops are used to repeat instructions.
# In python - while loop and for loop

# 1. WHILE LOOP
# Syntax
# while condition:
# some work

# while True:  #-> this prints infinitely!
#     print("Hello Sagar")

count = 1.0  # iterator
while count <= 5:
    print("Hello Sagar")
    count += 1

print(count)  # 6


# i = 1
# while i <= 100000:
#     print("Hello", i)
#     i += 1


i = 1
while i <= 5:
    print(i)
    i += 1
print("Loope ended!")

# Print numbers from 5 to 1

i = 5
while i >= 1:
    print(i)
    i -= 1

print("loops ended!")


### 1. Print numbers from 1 to 100.
i = 1
while i <= 100:
    print(i)
    i += 1
print("Printed from 1 to 100")

### 2. print numbers from 100 to 1
i = 100
while i >= 1:
    print(i)
    i -= 1
print("Printed from 100 to 1")

### 3. Print the multiplication of table of number n.

factor = 1
number = int(input("enter the number"))
while factor <= 10:
    mul = number * factor
    factor += 1
    print("the multiplication is ", mul)

### 4. Print the elements of the following list using a loop
# [1, 4,9, 16, 25, 36, 49, 64, 81, 100]

num = 1
array = []
while num <= 10:
    square = num**2
    array.append(square)
    num += 1
    print("square is :", square)

    print(array)
    
    
    ###ORED print-elemets only
    nums = [1,4, 9, 16, 25,36, 49, 64, 81,100]
    idx = 0
    while idx < len(nums):
        print(nums[idx]);
        idx += 1
    
