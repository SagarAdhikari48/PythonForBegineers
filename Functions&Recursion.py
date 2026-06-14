### FUnctions -> Block of statements that performs a specific task.

# def calculate_sum(a, b):
#     sum = a + b
#     print(sum)
#     return sum


# calculate_sum(4, 5)
# calculate_sum(9, 19)
# calculate_sum(55, 77)

#More simple 
#finction defition
def calculate_sum2(a, b): #parameters
    return a + b


sum = calculate_sum2(4, 6) # Function call; arguments
print(sum)


def print_hello(): # functions with no arguments
    print("Hello!")
    
print_hello()


output = print_hello()
print(output) # Output is None because the function is not returning anything! 


## Average of 3 numbers
def calculate_average(a, b, c):
    avg = (a + b + c) / 3
    print(avg)
    return avg

calculate_average(4, 5, 6)