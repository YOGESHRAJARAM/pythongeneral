#!/bin/env/python3
# the pice of code used to change the lines in the file to upper case

with open("sample.txt") as file :
    for line in file:
        print(line.upper())
        
#to reduse the unwanted space we have the use strip function in the program

with open("sample.txt") as file :
    for line in file:
        print(line.strip().upper())