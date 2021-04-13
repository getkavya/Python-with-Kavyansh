what=int(input("1.usd to inr\n2.inr to usd\nenter here:-   "))
us=73.18
inr1 = 0.013
if what== 1:
    inr = int(input("How much do you want to convert?\nEnter here-:\n"))
    print("INR =", inr*us)

elif what==2:
    usd = int(input("How much do you want to convert?\nEnter here-:\n"))   
    print("USD = ", usd*inr1)

else:
    print("Invalid Input")