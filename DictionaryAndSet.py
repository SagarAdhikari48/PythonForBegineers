# info = {
#     "name" : "Sagar",
#     "subjects" : ["Python", "Java", "C++"],
#     "topics" : ("Data Structures", "Algorithms", "OOP"),
#     "age": 35,
#     "is_adult": True,
#     "marks" : 80
# }

# print(info)
# print(info["name"])

# info["name"] = "Adhikari Sagar"
# info["newKey"] = "New Value"
# print(info)

#Nested Dictionary
student = {
    "name": "Sagar",
    "subjects": {"phy": 98, "chem": 99, "maths": 100},
    "topics": ("Data Structures", "Algorithms", "OOP"),
    "age": 35,
    "is_adult": True,
    "marks": 80,
}

print(student)
print(student["subjects"]["phy"])
