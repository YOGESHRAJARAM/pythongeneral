import os
import shutil
path="C:/Users/Yogesh/Downloads/testing/"
dirt_list=os.listdir(path)
print("here is the list of parth: ",dirt_list)
n=0
file_list=[]
sort_folder=[]
for list in dirt_list:
    ##print(dirt_list[n])
    extension=dirt_list[n].split(".")
    sort_folder.append(extension[-1])
    file_list.append(dirt_list[n])
    n=n+1
#print(file_list)
unique_list =[]
[unique_list.append(x) for x in sort_folder if x not in unique_list]
#print(unique_list)

b=0
for x in unique_list:  
  os.makedirs(path+unique_list[b])
  for i in file_list:
     if x in i: 
       print(x)
       print(i)
       print(path+i)
       print(path+x+i)
       shutil.move(path+i,path+(x+"/")+i)    
  b+=1
 
       




    
    