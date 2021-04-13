#lable #geometry #maximize #minimize
from tkinter import *
root = Tk()
#Logic here...

root.geometry("500x500")#First widthxheight in string 
root.minsize(300, 300)#First width, height in integer
root.maxsize(5000, 5000)#First width, height in integer
#Lable
Lable_manan = Label(text="I am testing my first lable with CodeWithHarry in his GUI tutorial.")
Lable_manan.pack()

root.mainloop()
 