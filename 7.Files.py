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

## r+ MODE 
f = open("demo.txt", "r+")
f.write("abc this will override the existing text in the file from the beginning of the file")
print(f.read())
f.close()
