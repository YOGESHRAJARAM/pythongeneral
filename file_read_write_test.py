#!\bin\env\python3
with open("sample.txt","r") as file:
    print(file.read())
    line=file.read()
file.close()
detail=input("please enter the test that you want to add in file")
with open("sample.txt","a") as file:
        print(file.write(detail + "/n"))
        
    
