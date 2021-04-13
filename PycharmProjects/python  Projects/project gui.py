from tkinter import *
import tkinter.messagebox as tmsg

root =Tk()

root.geometry("500x500")
root.title("PythonWithKavi")

var1 = StringVar()
user_input = StringVar()


#contact menu functions


def func1():
    tmsg.showinfo("Email", "kavimahehswari609@gmail.com")

def func2():
    tmsg.showinfo("Phone Number", "Call us on -- 7796637726")

def func3():
    message_root = Tk()

    message_root.geometry("200x100")
    message_root.title("Message")
    message_root.config(bg="yellow")

    mess = Entry( message_root, textvariable=var1).grid()
    Button(message_root, fg="black", text="Submit").grid()
    
    message_root.mainloop()


# help menu functions


def func4():
    kavyansh = Tk()

    kavyansh.title("Report")
    kavyansh.geometry("300x100")
    kavyansh.config(bg="light green")

    Label(kavyansh, text="Report").grid(row=0, column=0)
    input_1 = Entry(kavyansh, textvariable=user_input).grid(row=0, column=1)
    Button(kavyansh, fg="black", text="Submit", command=kavyansh.destroy).grid()

    kavyansh.mainloop()

def func5():

    answer = tmsg.askyesno("Rate Us", "Did you like our window?")

    if answer==YES:
        tmsg.showinfo("Thanks For Feedback", "Great, pls can you rate us on app store")

    else:
        tmsg.showinfo("Problem", "Tell us your problem\nContact us on-: 7796637726")   


# about menu functions


def func6():
    tmsg.showinfo("Creator", "Creator: Kavyansh Maheshwari")

def func7():
    tmsg.showinfo("Helper", "Helper: Manan Maheshwari")

def func8():
    tmsg.showinfo("Contact", "Contact (Microsoft Account): k120197@thebishopsschol.net\nPhone Number: 7796637726\nWhatsapp: 7796637726")

def func9():

    megha = Tk()

    megha.geometry("200x200")
    megha.title("Persnal Message")
    megha.config(bg="yellow")

    Label(megha, text="Message").grid()
    input_1 = Entry(megha, textvariable=user_input).grid(row=0, column=1)
    Button(megha, fg="black", text="Submit", relief=SUNKEN).grid()

    megha.mainloop()


# all menus


main = Menu(root)

# contact menu

menu1 = Menu(main, tearoff=0)
menu1.add_command(label="Email", command=func1)
menu1.add_command(label="Phone Number", command=func2)
menu1.add_command(label="Message", command=func3)
root.config(menu=main)
main.add_cascade(label="Contact", menu=menu1)


# help menu

menu2 = Menu(main, tearoff=0)
menu2.add_command(label="Report", command=func4)
menu2.add_command(label="Feedback", command=func5)
root.config(menu=main)
main.add_cascade(label="Help", menu=menu2)


# about menu

menu2 = Menu(main, tearoff=0)

menu2.add_command(label="Creator", command=func6)
menu2.add_command(label="Helper", command=func7)
menu2.add_command(label="Contact", command=func8)
menu2.add_command(label="Persnal Message", command=func9)

root.config(menu=main)
main.add_cascade(label="About", menu=menu2)

root.mainloop()