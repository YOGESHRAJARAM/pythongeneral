class complexnumber :
    def __init__(self,r,i):
        self.real= r
        self.imagin = i
    def __add__(self,other):
        return f"{self.real+other.real}+{self.imagin+other.imagin}"
        

c1=complexnumber(2,4)
c2=complexnumber(5,8)

print(c1+c2)

class persion:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __gt__(self,other):
        if(self.age>other.age):
            return True
        else:
            return False
        
p1=persion("ram",22)
p2=persion("yogesh",23)

if(p1>p2):
    print(f"{p1.name} will pay the bill")
else:
    print(f"{p2.name} will pay the bill")