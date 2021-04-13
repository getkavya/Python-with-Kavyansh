from tkinter import *
root = Tk()
root.geometry("600x400")

def inspiration():
    print("CodeWithHarry because of you harry bhai I have learnt this much in the age of 12.Thanka a lot!!!")

def name():
    print("kavyansh Maheshwari")

def dream():
    print("To beacome a software endineer with some knowladge of Web devolopment")

frame = Frame(root, borderwidth=6, background="green", relief=SUNKEN)
frame.pack(side=LEFT, anchor=NW)
#Buttons
button_1 = Button(frame, fg="blue", text="My inspiration", command=inspiration)
button_1.pack(side=LEFT)
button_2 = Button(frame, fg="blue", text="My dream", command=dream)
button_2.pack(side=LEFT, padx=9)
button_3 = Button(frame, fg="blue", text="My Name", command=name)
button_3.pack(side=LEFT, padx=9)

root.mainloop()