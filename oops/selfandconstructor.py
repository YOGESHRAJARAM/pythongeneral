class human:
    def __init__(self):
        self.age =20
        self.height=180
    def update(self):
        self.height=220
    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False
            

        
ramesh=human()
suresh=human()
print(ramesh.age)
ramesh.age=35
print(ramesh.height)
ramesh.update()
print(ramesh.age)
print(ramesh.height)

print(suresh.age)

if ramesh.compare(suresh):
    print("yes they are same")
    print(suresh.age)
else:
    print("no they are not same")
