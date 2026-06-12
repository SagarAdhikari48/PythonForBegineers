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







## Set in Python. -> Sets are mutable but elements inside it are immutable
    # Set is the collection of the unordered - no indexed items
    # Each elements in the sets must be unique -(we will not set number ,value,string twice) and immutable- (menas we can store numbers,integer and floats)
##BUt we cannot store list and dictionary in a set because they are mutable(means we can change list and dictionary as we already did above using different methods)

collection = {1, 2, 2, 3,4, "hello", "world" ,"world",5} # We can also store string values within set and aslo duplicate value in a set but the set ignore the duplication.

print(collection)
print(type(collection))  
print("length: ",len(collection))    
    #The output of the set will output randomly - {1, 2, 3, 4, 5, 'hello', 'world'} - but removes duplicates


## Empty Sets
collection = {} # Empty Dictionary
print(type(collection))

collection = set() # Empty Sets
print(type(collection))

## MEthods in sets
# Sets are mutable
# Elements in sets are not immutable


setCollection = set()

setCollection.add(1)
setCollection.add(2)
setCollection.add(3)
setCollection.add(2) #Duplication are removed!
setCollection.add(4)
setCollection.add("Sagar Adhikari")
setCollection.add("Married")
setCollection.add("Amrita Gautam")
setCollection.add((1,2,3,4))
# setCollection.add([1,2,3,4]) #Error - TypeError: cannot use 'list' as a set element (unhashable type: 'list')- since list are mutable and the hash value will be different upon the list value changed 


print("Set collection : ",setCollection)


## Clear Method - Completely empty our sets
collection = {1, 2, 2, 3,4, "hello", "world" ,"world",5} 
print("collection: ",collection)
print("Clear Collection: ",collection.clear())

# Pop Method - pops any random items from sets
pop_collection = {1, 2, 2, 3,4, "hello", "world" ,"world",5} 
print("Pop methods 1 : ",pop_collection.pop())
print("Pop methods second pop item : ",pop_collection.pop())

## Union Method -> Combines bot set values and return new

set1 = {1, 2, 3}
set2 = {2,3,4}
print("Union Method : ", set1.union(set2))



## Intersection Method -> Combines common values and return new
set1 = {1, 2, 3}
set2 = {2,3,4}
print("Intersection Method : ", set1.intersection(set2))


### Challenge -1 -> Store following word meanings in a python dictionary
    # table :"a piece of furniture" , "list of facts and figures"
    # cat: "a small animal"
    
dict = {
    "table": ["a piece of furniture", "list of facts and figures"],
    "cat":"a small animal"
}