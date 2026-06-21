# Challenge #6: Find Sum of Array
# [10, 20, 30, 40]


def sum_of_array(array):
    sum = 0
    for i in range(0, len(array)):
        sum += array[i]
    # print(sum)


sum_of_array([10, 20, 30, 40])


# Challenge #7: Find Average of Numbers
# [10, 20, 30, 40, 50]


def find_average_in_array(arr):
    sum = 0
    average = 0
    for i in range(0, len(arr)):
        sum += arr[i]
        average = sum / len(arr)
    print("average is: ", average)


# find_average_in_array([10, 20, 30, 40, 50])


# Challenge #8: Count Occurrences of a Character
# hello
# l - 2


def calculate_count_in_string(value, target):
    count = 0

    for char in value:
        if char == target:
            count += 1
    return count


# print(calculate_count_in_string("hello", "l"))


# Challenge #9: Remove Duplicates from Array
# [1, 2, 2, 3, 4, 4, 5]


def remove_duplicates(numbers):
    return list(set(numbers))


print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))
