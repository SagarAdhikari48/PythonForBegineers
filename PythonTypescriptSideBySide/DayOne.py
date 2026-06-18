#  Challenge #1: Find Even or Odd
def find_even_or_odd(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")


# find_even_or_odd(10)
# find_even_or_odd(9)


# Challenge #2
# Find the largest Number from an array
def find_largest_number(nums):
    largest = nums[0]
    for i in range(0, len(nums)):
        print(i)
        if nums[i] > largest:
            largest = nums[i]
            i += 1
    print("The largest number in the list is : ", largest)


# find_largest_number([4, 10, 7, 99, 5, 120])

# ORED


def find_largest(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest


# print("Largest : ",find_largest([1, 3, 6, 90, 44, 36]))

# 3 .Reverse a string without using built-in reverse functions.

def find_reverse_of_string(value):
    reversed_string = ""
    for i in range(0, len(value)):
        reversed_string = value[i] + reversed_string
        i += 1
    return reversed_string
        
        
# print(find_reverse_of_string("Hello"))

# Ored
def find_reverse2(text):
    reversed = ""
    for ch in text:
        reversed = ch + reversed
    return reversed
# print(find_reverse2("Sagar"))