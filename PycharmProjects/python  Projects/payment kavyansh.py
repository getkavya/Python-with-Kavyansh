# Payment Function Credit Card
def Payment():
    """This is function which will do online credit card payment
       it will take input of cardno, , expiry  , owner, and amount cvv.
       It will also tale your email and after transection one email
       will be send to the email which you have entered in the input.
       This will work as a replacement of human to ai for online payment."""

    name = input("Whats Your good Name sir/maam\n"
                 "Enter Here:- ")
    print("Ok", name, "Nice to meet you")

    cardno = int(input("Enter Your card no.:-  "))
    c = cardno + 0
    if c>999999999999:
        while True:
                print("Invalid Input")
                D = int(input("Enter cardno. :- "))
                if D + 0<+999999999999:
                    break
                else:
                    pass
    elif c<+999999999999:
        pass

    expirydate = int(input("Enter card expiry:- "))
    if expirydate>9999 or expirydate<=999:
        while True:
                print("Invalid Input")
                F = int(input("Enter cvv:- "))                 
                if F + 0 <= 9999 and F + 0 >=999:
                    break

    elif expirydate >=9999 and expirydate >= 999:
        pass
    cardowner = str((input("Enter Card Owner Name:- ")))
    cvv = int(input("Enter cvv:- "))
    a = cvv + 0
    if a>999 or a<=99:
        while True:
                print("Invalid Input")
                B = int(input("Enter cvv:- "))                 
                if B + 0 <= 999 and B + 0 >=99:
                    break

    elif a >=999 and a >= 99:
        pass
    email = (input("Whats your Gmail:- "))
    print()
    amount = str(input("Whats the amount rupees:-"))
    print("Pls confirm your details:-")
    try:
       print("CVV - ", D)
    except:
        print("cardno. - ", cardno)
    print("Expiry Date", expirydate)
    print("Card Owner - ", cardowner)
    try:
       print("CVV - ", B)
    except:
        print("CVV - ", cvv)
    print("Amount", amount)
    print("Gmail:- ", email)
    print()
    comform = str(input("Conform? yes or no\n"
                        "enter here:- "))
    if comform== "yes":
        print("Payment Succesfull")
    else:
        print()
        print("Ok", name, "Do Payment again:-\n")
        Payment()
    def sendEmail(to, content):
        import smtplib
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('kavimaheshwari609@gmail.com', '#kavyanshhero@9548')
        server.sendmail('kavimaheshwari609@gmail.com', to, content)
        server.close()
    try:
        content = f"\nPythonWithManan:- Park Transaction\nYour transaction of rupees {amount} is completed\nThank you for visiting our park\nPlease come again to our park\n"
        to = email
        sendEmail(to, content)
        print("Email has been sent to", email)
    except Exception as e:
        print(e)
        print("Sorry sir kavyansh. I am not able to send this email")
Payment()        