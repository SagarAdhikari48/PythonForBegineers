# Challenge #6: Find Sum of Array
# [10, 20, 30, 40]


def sum_of_array(array):
    sum = 0
    for i in range(0, len(array)):
        sum += array[i]
    print(sum)


sum_of_array([10, 20, 30, 40])
