## Python can be used to perform operations on a file.(read & write data)
##types of files 1. Text Files: .txt, .docs, .log etc
# 2. Binary Files: .mp4, .mov, .png, .jpeg etc

f = open("demo.txt", "rt") # if in case the  location of text file is any other location we have to provide complete path /Users/sagar/work/python/demo.txt
data = f.read()
print(data)
print(type(data))
f.close()
