from tkinter import *

def getvals():
    print(f"The value of username is {User_Var.get()}")
    print(f"The value of password is {Password_Var.get()}")


root = Tk()
root.geometry("500x400")

lable_Username = Label(root, text="UserName")
lable_Username.grid()
lable_password = Label(root, text="Password")
lable_password.grid()

#Varriable Classes in Tkinter..
"""
Boolean Varriable
Doublevar Varriable
Integer Varriable
String Variable
"""

User_Var = StringVar()
Password_Var = StringVar()

Entry_user = Entry(root, textvariable=User_Var)
Entry_user.grid(row=0, column=1)

Entry_Password = Entry(root, textvariable=Password_Var)
Entry_Password.grid(row=1, column=1)

Button(text="Submit", command=getvals).grid()


root.mainloop()