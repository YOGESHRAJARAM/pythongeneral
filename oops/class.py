"""""
class student:
    def __init__(self) -> None:
        self.name="Yogesh R"
        self.register_number="18itu063"   
    def display(self) -> None:
        print("student Name",self.name)
        print("student register number",self.register_number)
        #None
        
s1=student()
s2=student()


print(s1.display())
print(s2.display())

"""""

# creating class called fruit 
"""""
class fruit:
    def __init__(self,col):
         self.color=col
apple=fruit("red")

print(apple.color)
        
"""""

#creating class called teacher
"""""
class teacher:
    def __init__(self,Name,register_number):
        self.name=Name
        self.register_num=register_number
    def display(self):
        print("Name :",self.name)
        print("register number :",self.register_num)
t1=teacher("saranya","18itu089")
t2=teacher("sanjay","1920uo90")
t1.display()
t2.display()
"""""

#creating calculator

class calculator:
    def __init__(self,a,b):
         self.num1=a
         self.num2=b
    def add(self):
        print("the Total sum of value is :",self.num1 + self.num2)
    def sub(self):
        print("the Total sum of value is :",self.num1 - self.num2)
    def multi(self):
        print("the Total sum of value is :",self.num1 * self.num2)
    def devi(self):
        print("the Total sum of value is :",self.num1 /self.num2)
my=calculator(5,4)
my.add()
        
