print("welcome to converter")
print("please enter the values in the hole numbers")
choois=input("please type 'c' to find celsius or 'f' to find fahrenheit :")

def celsius1(n):
    print("celsius-converter")
    output=(int(n)-32)*5/9
    print("the number of ",n," fahrenheit is equal to",round(output,2),"celsius..")
    
def fahrenheit(n):
    print("fahrenheit-converter")
    output=(int(n*9/5)+32)
    print("the number of ",n," celsius is equal to",round(output,2),"fahrenheit..")

if choois == 'c': 
    num=int(input("please enter the number in fahrenheit :"))
    celsius1(num)
else:
     num=int(input("please enter the number in celsius :"))
     fahrenheit(num)
