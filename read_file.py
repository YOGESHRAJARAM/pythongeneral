#!/bin/env/python3
# this below line comment will help you to print line by line text 

file=open("sample.txt")
print(file.readline())
print("-------------")

# this below command will print the hole file in the terminal

print(file.read())

file.close()

# (with open) commend will help us to close the file without using file.close()

#example:
''' with open("sample.txt") as file '''
