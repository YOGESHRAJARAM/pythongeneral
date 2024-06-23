import math
def main():
    card_no_orgi = int(input("Enter yout card number please: -- "))
    validate_count(card_no_orgi)
    if card_number == 16:
      print("step 1 ","card has 16 number")
      number_seperat(card_no_orgi)
      print("step 4 after seperate",seperated_num)
      multipleByTwo()
      splitAndAdd(moretheten)
      totalofall()
      if int(firstdegit) == int(afterlast_remove):
          print("the card is valid---------------")
      else:
          print("invalid card")
      
    

    else:
      print("please enter valide number you gives only "+str(card_number)+" number")
      main()

def validate_count(a):
     global card_number
     card_number=len(str(a))
     
     

def number_seperat(a):
    #global last_number
    global afterlast_remove
    global seperated_num
    seperated_num = [int(x) for x in str(a)]
    print("step 2 seperated number",seperated_num)
    #last_number = seperated_num[-1]
    afterlast_remove = seperated_num.pop(-1)
    print("step 3 that last number",afterlast_remove)

    return seperated_num 

def multipleByTwo():
    global moretheten
    global lessthanten
    global numberun_select
    global totalofless
    numberun_select=[seperated_num[1],seperated_num[3],seperated_num[5],seperated_num[7],seperated_num[9],
                     seperated_num[11],seperated_num[13]]
    number_select=[2*seperated_num[0],2*(seperated_num[2]),2*(seperated_num[4])
                   ,2*(seperated_num[6]),2*(seperated_num[8]),2*(seperated_num[10])
                   ,2*(seperated_num[12]),2*(seperated_num[14])]
    print("step 5 split and multiple by 2 ",number_select)
    moretheten = []
    lessthanten = []
    k=10
    for i in number_select:
        if i >= k:
            moretheten.append(i)
        else:
            lessthanten.append(i)
    
    
    print("step 6 more than ten ",moretheten ,"less than ten ",lessthanten)
    totalofless=0
    for x in lessthanten:
        totalofless+= int(x)
        
        
  
def splitAndAdd(s):
    global total
    namestor=[]
    for i in s:
        namestor += str(i)
    print("step 7 ",namestor)

    total = 0
    for x in range(0,len(namestor)):
        total += int(namestor[x])
   # print(total)

def totalofall():
    global finalTotal
    #print(numberun_select)
    Totalofa=0
    for x in numberun_select:
        Totalofa+= int(x)
    ##print(Totalofa)
    ##print(totalofless)
    finalTotal= int(total)+int(Totalofa)+int(totalofless)
    print("we got the total = ",finalTotal)
    result=str(finalTotal)
    global firstdegit
    if finalTotal >= 100:
         resultlist=list(result)
        
         addresult= str(resultlist[0])+str(resultlist[1])
         firstdegit= 10 - int(resultlist[2])
         return firstdegit
    else:
        
          resultlist=list(result)
          firstdegit=10 - int(resultlist[1])
          return firstdegit
    
            

main()
    

    
