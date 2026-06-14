### FUnctions -> Block of statements that performs a specific task.

# def calculate_sum(a, b):
#     sum = a + b
#     print(sum)
#     return sum


# calculate_sum(4, 5)
# calculate_sum(9, 19)
# calculate_sum(55, 77)

# More simple
# finction defition
# def calculate_sum2(a, b): #parameters
#     return a + b


# sum = calculate_sum2(4, 6) # Function call; arguments
# print(sum)


# def print_hello(): # functions with no arguments
#     print("Hello!")

# print_hello()


# output = print_hello()
# print(output) # Output is None because the function is not returning anything!


# ## Average of 3 numbers
# def calculate_average(a, b, c):
#     avg = (a + b + c) / 3
#     print(avg)
#     return avg

# calculate_average(4, 5, 6)


### Types of Functions: 1. Built-in Functions -> print(), len(), type(), range(), etc
#   2. User Defined Functions -> funtion made by programmer.


# def calculate_prod(a = 3, b = 4): # Default parameters
#     return a * b


# prod = calculate_prod()
# print(prod)


# def calculate_prod(a , b = 4): # Default parameters
#     return a * b


# prod = calculate_prod(1)
# print(prod)


# def calculate_prod(a = 5 , b ): ##this cannot be written # Non-default argument follows default argument
#     return a * b


# prod = calculate_prod(1)
# print(prod)


####1. WAP to print the length in a list. (List is the parameter)

# nums = [1, 4, 6, 7, 8, 9, 0]
# cities = ["ktm", "Bkt", "Ltr", "Nuwakot"]


# def calculate_length(list):
#     print(len(list))


# calculate_length(nums)
# calculate_length(cities)

###3. WAP to find the element of list in a single line. (list is the parameter)

# cities = ["Nuwakot", "Kathmandu", "Pokhara", "Biratnagar", "Dhulikhel"]
# def display_element_in_line(list):
#     for item in list:
#         print(item, end=" ") # this leaves % in the last to remove  this use extra print at last
        
# display_element_in_line(cities)
# print()

# ###4. WAP to find the factorial of n.(n is the parameter)

# def calculate_factorial(n):
#     fact =1
#     for i in range(1, n+1):
#         fact *= i
#     print(fact)
        
# calculate_factorial(5)

###5. Convert to dollar to npr 
def convert(usd):
    npr = usd * 152.08
    print(usd, "USD = " ,npr ,"NPR");
    
convert(100)


###6. Function to calculate odd or even 
def find_odd_or_even(num):
    if(num % 2 == 0):
        print("the number is EVEN")
    else:
        print("The number is ODD")
        
find_odd_or_even(40)
find_odd_or_even(39)
