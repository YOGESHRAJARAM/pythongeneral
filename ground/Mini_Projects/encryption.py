print("please dont enter simples like !@#$ eg...")
name=input("enter the string to change in to encrypted :")
length=len(name)
for i in range (length):
    for j in name:
        
        if "a" in name:
            name=name.replace("a","1")
        elif "b"in name:
            name=name.replace("b","2")
        elif "c"in name:
            name=name.replace("c","3")
        elif "d"in name:
            name=name.replace("d","4")
        elif "e"in name:
            name=name.replace("e","5")
        elif "f"in name:
            name=name.replace("f","6")
        elif "g"in name:
            name=name.replace("g","7")
        elif "h"in name:
            name=name.replace("h","8")
        elif "i"in name:
            name=name.replace("i","9")
        elif "j"in name:
            name=name.replace("j","10")
        elif "k"in name:
            name=name.replace("k","11")
        elif "l"in name:
            name=name.replace("l","12")
        elif "m"in name:
            name=name.replace("m","13")
        elif "n"in name:
            name=name.replace("n","14")
        elif "o"in name:
            name=name.replace("o","15")
        elif "p"in name:
            name=name.replace("p","16")
        elif "q"in name:
            name=name.replace("q","17")
        elif "r"in name:
            name=name.replace("r","18")
        elif "s"in name:
            name=name.replace("s","19")
        elif "t"in name:
            name=name.replace("t","20")
        elif "u"in name:
            name=name.replace("u","21")
        elif "v"in name:
            name=name.replace("v","22")
        elif "w"in name:
            name=name.replace("w","23")
        elif "x"in name:
            name=name.replace("x","24")
        elif "y"in name:
            name=name.replace("y","25")
        elif "z"in name:
            name=name.replace("z","26")
        
print("your encrypted code is :",name)

    

    