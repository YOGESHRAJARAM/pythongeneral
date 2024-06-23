file = open("sample.txt")
line=file.readlines()
file.close()

# even thouth we close the file it will store the line in the line variable
# this will reduse the memory usage or background data usage for the same file 

print(line)