## Python can be used to perform operations on a file.(read & write data)
##types of files 1. Text Files: .txt, .docs, .log etc
# 2. Binary Files: .mp4, .mov, .png, .jpeg etc


###OPEN and READ
# f = open("demo.txt", "rt") # if in case the  location of text file is any other location we have to provide complete path /Users/sagar/work/python/demo.txt
# data = f.read()
# print(data)
# print(type(data))
# f.close()


# f = open("demo.txt", "rt") # if in case the  location of text file is any other location we have to provide complete path /Users/sagar/work/python/demo.txt
# data = f.read(5) # read upto 5 characters
# print(data)
# print(type(data))
# f.close()


# f = open("demo.txt", "rt") # if in case the  location of text file is any other location we have to provide complete path /Users/sagar/work/python/demo.txt
# line1 = f.readline() # read only one line
# print(line1)
# # Space will occurs in the output after readline one , two and so on.
# line2 = f.readline() # read only second line
# print(line2)
# f.close()


### WRITING TO A FILE - open file in "w" write override mode or "a" append mode - add at the end
# f = open("demo.txt", "w")
# f.write("I am opening file in write overrde method which will completely overrides the existing file and replace by this text")
# f.close()

##APPEND MODE
# f = open("demo.txt", "a")
# f.write("\nI am opening file in append method which will add the text after existing text in a file")
# f.close()

##NO FILE WAS CREATED AND TRIED TO OPEN (In write mode)

# f = open("sample.txt", "w")
# f.close()

##NO FILE WAS CREATED AND TRIED TO OPEN (In append mode)
# f = open("sample1.txt", "a")
# f.close()

# ## r+ MODE 
# f = open("demo.txt", "r+")
# f.write("abc this will override the existing text in the file from the beginning of the file")
# print(f.read())
# f.close()


# ## w+ MODE - file open in truncated - completely wiped out mode and write the text in the file and then read the text from the file
# #This will print nothing because the file is opened in write mode and the pointer is at the end of the file after writing the text in the file. So we have to move the pointer
# # #f.seek(0)  # Move the pointer to the beginning of the file - this will move the pointer to the beginning of the file using seek() method.
# f = open("demo.txt", "w+")
# f.write("w+ mode")
# # f.seek(0)  # Move the pointer to the beginning of the file
# print(f.read())
# f.close()



# ## a+ MODE - file open in append mode and write the text in the file and then read the text from the file
# #This will print nothing because the file is opened in append mode and the pointer is at the end of the file after writing the text in the file. So we have to move the pointer
# # #f.seek(0)  # Move the pointer to the beginning of the file - this will move the pointer to the beginning of the file using seek() method.
# f = open("demo.txt", "a+")
# f.write("a+ mode")
# # f.seek(0)  # Move the pointer to the beginning of the file
# print(f.read())
# f.close()


### WITH SYNTAX - No need to close file in this syntax it automatically closes the file
# with open("demo.txt","a") as f:
# data = f.read()

# with open("demo.txt", "r") as f:
#     data = f.read()
#     print(data)
    
# with open("demot.txt", "w") as f:
#     f.write("This is a write mode with syntax")
    
    
### DELETING A FILE - using the os module we cannot delete a file using the built in function but we can use the os module to delete a file. os module is a built in module in python which provides functions to interact with the operating system.
# Module like code library is a file written by another programmer that fenerally has a functions we can use.
# import os
#os.remove(filename)


import os
os.remove("sample.txt")
