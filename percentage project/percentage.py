import random
import math
def welcome():
    print("welcome to the presentage calculation program")   
def generator():
    num1=random.randint(1, 10000)
    num2=random.randint(1,100)
    print("find the",num2,"persentage of ",num1)
    answer=input("please enter your answer :")
    result=num2/100*num1
    if answer==str(math.ceil(result)):
        return"correct"
    else:
        print("wrong")
        return math.ceil(result) 
welcome() 
for i in range(10):
      i=i+1
      print("Question number :", i)
      print(generator())
print("------Over if you want re-test please run the program again------")

