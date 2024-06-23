#!/bin/env/python3
file = open("sample2.txt","r")
line = file.read()
file.close()
with open("sample2.txt","w") as file2:
    
  print(".......................")
  file2.write(line.upper()) #You can conver to lowercase by changing (line.upper()) into (line.lower)
  
# file.write("tamil nadu is very great")
# file.close()



'''
open for reading (default)

'w'

open for writing, truncating the file first

'x'

open for exclusive creation, failing if the file already exists

'a'

open for writing, appending to the end of file if it exists

'b'

binary mode

't'

text mode (default)

'+'

open for updating (reading and writing)
'''