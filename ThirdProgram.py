# Lists and Tuples in python

# slicing list

# marks = [85, 94, 76, 63, 48]
# print(marks[1 : 4])
# print(marks[1 : ])
# print(marks[-3 : -1])


# List Methods

# list = [2, 3, 1]
# list.append(4)
# print(list)
# list.sort()
# print(list)
# list.sort(reverse=True)
# print(list)
# list.reverse()
# print(list)
# list = list.insert(2, 3)
# print(list)


# Tuples in python programming
# - immutable that cannot be change/update as list
# -tuple are written inside parenthesis

# tup = (2, 1, 3, 1)
# print(type(tup))
# print(tup[2])


# Check pallindrome [1,2,3,2,1] = [1,2,3,2,1]

list1 = ["a", "b", "c", "d"]
list2 = [1, 2, 3, 4]

copy_list = list1.copy()
copy_list.reverse()

if(copy_list == list1):
    print("Pallindrome")
else: 
    print("Not Pallindrome")
