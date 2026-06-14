## Python can be used to perform operations on a file.(read & write data)
##types of files 1. Text Files: .txt, .docs, .log etc
# 2. Binary Files: .mp4, .mov, .png, .jpeg etc

f = open("demo.txt", "r")
data = f.read()
print(data)
print(type(data))
f.close()
