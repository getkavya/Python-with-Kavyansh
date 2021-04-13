from tkinter import *
import datetime
import random
def checkin():
    kavi = Tk()
    kavi.geometry("690x600")
    kavi.title("Check In")
    kavi.config(bg="light green")

    # users info
    Label(kavi, text="Hotel Managment By Kavyansh", font="comicsansMS 25 bold", bg="light green").grid(row=2 , column=1)
    Label(kavi, text="Name", font="comicsansMS 20 bold", bg="light green").grid(row=3 , column=0)
    Label(kavi, text="Gender", font="comicsansMS 20 bold", bg="light green").grid(row=4 , column=0)
    Label(kavi, text="Email", font="comicsansMS 20 bold", bg="light green").grid(row=5 , column=0)
    Label(kavi, text="Contact", font="comicsansMS 20 bold", bg="light green").grid(row=6 , column=0)
    

    
    gender = StringVar() 
    email = StringVar()
    phone = StringVar()
    

    name = Entry(kavi, textvar=StringVar(), font="lucida 20 bold").grid(row=3, column=1)
    Entry(kavi, textvar=gender, font="lucida 20 bold").grid(row=4, column=1)
    Entry(kavi, textvar=email, font="lucida 20 bold").grid(row=5, column=1)
    Entry(kavi, textvar=phone, font="lucida 20 bold").grid(row=6, column=1)

    # payment mode
    var = StringVar()
    var.set("radio")

    Label(kavi, text="Payment Mode", font="comicsansMS 20 bold", bg="light green", fg="red").grid(row=9, column=0)
    radio = Radiobutton(kavi, text="Google Pay", variable=var, value="Google Pay", font="comicsansMS 10 bold").grid(row=10, column=0)
    radio = Radiobutton(kavi, text="Credit Card", variable=var, value="Credit Card", font="comicsansMS 10 bold").grid(row=11, column=0)
    radio = Radiobutton(kavi, text="Debit Card", variable=var, value="Debit Card", font="comicsansMS 10 bold").grid(row=12, column=0)
    radio = Radiobutton(kavi, text="BHIM", variable=var, value="BHIM", font="comicsansMS 10 bold").grid(row=13, column=0)

    def save():
        today_date = datetime.date.today()

        with open("test.txt", "w") as f:
            f.write(f"name - {name}\n")
            f.write(f"gender - {gender}\n")
            f.write(f"Date - {today_date}\n")
            f.write(f"------------------------------------\n")
            f.close()

    b10 = Button(kavi, text="Submit", font ="comicsansMS 20 bold", command=save).grid()

    
   

    kavi.mainloop()


def checkout():
    check_out = Tk()
    check_out.geometry("500x350")
    check_out.title("Check Out")
    check_out.config(bg="orange")

    Label(check_out, text="Check Out -", font="comicsansMS 20 bold", bg="orange").grid()
    Label(check_out, text="Room No.", font="comicsansMS 30 bold", bg="orange").grid(row=1, column=0)
    Label(check_out, text="Name", font="comicsansMS 30 bold", bg="orange").grid(row=2, column=0)

    room_no = StringVar() 
    name2 = StringVar()
    Entry(check_out, textvar=room_no, font="lucida 20 bold").grid(row=1, column=1)
    Entry(check_out, textvar=name2, font="lucida 20 bold").grid(row=2, column=1)
    m = Button(check_out, text="Check Out", font="comicsansMS 15 bold").grid()

    check_out.mainloop()
    

def roomkey():
    
    
    aayu = Tk()
    aayu.title("Room Key")
    aayu.geometry("350x150")
    aayu.config(bg="pink")

    key = random.randint(100, 1000)

    Label(aayu, text="Your Room Key Is", font="comicsansMS 30 bold").grid()
    Label(aayu, text=key, font="algergian 20 bold").grid()
    room = Button(aayu, text="OK", font="comicsansMS 15 bold").grid()

    aayu.mainloop()





root = Tk()
root.geometry("500x400")
root.title("Hotel Kavyansh")
root.config(bg="light blue")
b1 = Button(root, text="Check In", font ="comicsansMS 10 bold", command=checkin).pack(ipadx=25, ipady=20, pady=10, padx=160, anchor=CENTER)
b2 = Button(root, text="Check Out", font ="comicsansMS 10 bold", command=checkout).pack(ipadx=20, ipady=20, pady=10, padx=160, anchor=CENTER)
b3 = Button(root, text="Exit", font ="comicsansMS 10 bold", command=quit).pack(ipadx=43, ipady=20, pady=10, padx=160, anchor=CENTER)


root.mainloop()
