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
#keys method - return all keys
print(student.keys())
print(student)
print(student["subjects"]["phy"])

#length of dictionary
print("Length : ",len(student))

#typecasting dictionary to list and tuples
print("List typecasting : ",list(student.keys()))

#values method -return all values
print(list(student.values()))

#item-method -return all key-value pairs as tuples within parenthesis comma seperated (key,values)
print("Item method: ",student.items())  # Item method:  dict_items([('name', 'Sagar'), ('subjects', {'phy': 98, 'chem': 99, 'maths': 100}), ('topics', ('Data Structures', 'Algorithms', 'OOP')), ('age', 35), ('is_adult', True), ('marks', 80)])

# access pairs of tuples 
pairs = list(student.items())
print(pairs[1]) #second tuples is pairs of 1.

#get method - returns the key according to value 2 method
    # dict["key"] =  values
    # dict.get("key") = values
    
print("diirect keys method : ",student["name"])
print("get method in dictionary :",student.get("name"))

#BUT if accidentaly typed key that is not in dictionary
# print("diirect keys method : ",student["name2"])  # this will throws error
print("get method in dictionary :",student.get("name2")) # This will not throw error but -> None


# update-method -> Inserts the specified items to the dictionary
new_dictionary = {"city" : "Kathamndu", "tole" : "Phutung" }
student.update(new_dictionary)
print("Update student : ",student)







## Set in Python
    # Set is the collection of the unordered - no indexed items
    # Each elements in the sets must be unique -(we will not set number ,value,string twice) and immutable- (menas we can store numbers,integer and floats)
##BUt we cannot store list and dictionary in a set because they are mutable(means we can change list and dictionary as we already did above using different methods)

collection = {1, 2, 3,4}

print(collection)
print(type(collection))    
