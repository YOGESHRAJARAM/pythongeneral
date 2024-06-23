print("  ! welcome to coconut profit calculator !  ")
no_coconut=int(input("Enter the number of coconut :  "))
Weight_co=float(input("Enter avarage weight of each coconut ( eg: 0.4 for 400 grams ) : "))
time_of_p=float(input("Enter the price of coconut per number at the time of purches :  "))
sell_ton=int(input("Enter the price of coconut per Ton :  "))



def income():
    weigh_c = 1000/Weight_co
    no_t= no_coconut/200*20
    
    no_coconut_t= no_t + no_coconut
    no_of_ton_available = no_coconut_t/weigh_c
    price_of_buying = no_coconut*time_of_p
    
    selling = no_of_ton_available*sell_ton
    profit = round(selling - price_of_buying)
    each_no = profit/no_coconut
    perse = each_no/time_of_p*100
    if profit>=1000:
        

      print("")
      print("-----Result-----")
      print("")
      print("The amount of profit that you can earn is =",profit,"Rs.. , You got=", round(each_no,3),"Rs.. as the profit per no of coconnut")
      print("It's around ", round(perse,2),"%")
      print("Price of buying =",price_of_buying ," ,   price of selling =",round(selling,2)) 
      print("")   
      print(" The above result are only the chance or approx to origenal result ma be + or - 1000 RS....")
      print("")
      print("")
      
    elif profit>=1:
      print("")
      print("-----Result-----")
      print("low profit ----")
      print("The amount of profit that you can earn is =",profit,"Rs.. , You got=", round(each_no,3),"Rs.. as the profit per no of coconnut")
      print("It's around ", round(perse,2),"%")
      print("Price of buying =",price_of_buying ," ,   price of selling =",round(selling,2)) 
    else:
        print(".....loss......")
      
    
    
    

income()
