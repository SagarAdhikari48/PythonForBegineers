# str1 = "this is a string"
# str2 = """this is a string"""
# str3 = "this is a string"


# # Escape Sequences
# str1 = "This is a string.\tWe are creating string in python programming!"
# print(str1)


# string1 = "Sagar"
# string2 = "Adhikari"
# print(string1 + " " + string2)

# print(len(string1))

# ch = string1[0]
# print(ch)


# Slicing is accessing parts of a string

# string = "I am sagar adhikari with seven year of experience in the field of software development!"
# stringSliced = string[1:4]  # 1,2,3
# print(stringSliced)
# print(string[5 :])
# print(string[: 5])

# print(string[-4: -1]) #kar
# print(string.endswith("development!"))
# print(string.capitalize())
# print(string.replace("seven", "7"))
# print(string.find("o"))
# print(string.count("o"));


# Conditionals statements

# age = int(21)
# if(age >= 18):
#     print("Can vote and can drive")

# elif(age <= 18):
#     print("You cannot drive and Vote")
# else :
#     print("Nothing")


# marks = int(input("Enter the marks obtained : "))

# if marks >= 90:
#     grade = "A"
# elif marks >= 80:
#     grade = "B"
# elif marks >= 70:
#     grade = "C"
# else:
#     grade = "D"

# print("grade of the Student : ", grade)



# Nesting loop in 
age = int(input("enter the age : ")) 

if(age >= 18) :
    if(age >= 80):
        print("you cannot drive")
    else:
        print("you can drive")
else:
    print("You cannot drive")
    
print("LOL")