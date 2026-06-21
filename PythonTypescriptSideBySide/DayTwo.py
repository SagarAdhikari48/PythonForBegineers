# Challenge #6: Find Sum of Array
# [10, 20, 30, 40]


def sum_of_array(array):
    sum = 0
    for i in range(0, len(array)):
        sum += array[i]
    print(sum)


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


find_average_in_array([10, 20, 30, 40, 50])
