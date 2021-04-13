import random
print("   HI, I will help you to decide what you want to eat.\n")
diet = str(input("1.Breakfast\n2.Lunch\n3.Dinner\n4.desert\n"))
if diet=="breakfast":    
    choice = input("1.carbohydrate , 2.protein\n")

    if choice=="carbohydrate":
        carbohydrate = (" poha"," upma"," vegetable sandwhich")
        print(random.choice(carbohydrate))

    elif choice=="protein":
        protein = (" paneer", " soyachunks", " oats ka chilla")
        print(random.choice(protein))

    else:
        print("Invalid Input")   

elif diet=="lunch":
    v3 = input("1.fatty , 2.healthy\n")  

    if v3=="fatty":
        fatty = (" pav bhaji"," pani puri") 
        print(random.choice(fatty)) 

    elif v3=="healthy":
        kavi = (" dal"," salad"," buttermilk")
        print(random.choice(kavi))  
    else:
        print("Invalid Input")
         
elif diet=="dinner":
    kav = input("1.balanced diet , 2.protein , 3.carbohydrate\n")      

    if kav=="balanced diet":
        v4 = (" dal"," sabji"," roti")
        print(random.choice(v4))  

    elif kav=="protein":
        v10 = (" eggs"," dal flour"," quinoa pulav")
        print(random.choice(v10))

    elif kav=="carbohydrate":
        v11 = (" biryani"," dosa", " idli")    
        print(random.choice(v11))

    else:   
        print("Invalid Input")

elif diet=="desert":
    ka = input("1.ice cream , 2.cold drink\n")
    if ka=="ice cream":
        v6 = (" vanilla"," chocolate"," pista")
        print(random.choice(v6))

    elif ka=="cold drink":
        v7 = (" fanta"," pepsi"," coca cola"," thumps up",)    
        print(random.choice(v7))
    else:
        print("invalid input")    

else:
    print("invalid input")

    






                