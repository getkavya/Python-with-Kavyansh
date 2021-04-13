from tkinter import *
from pil import Image, ImageTk
root = Tk()

root.geometry("1000x800")
#for png images follow this
"""
image_lable = Label(image=photo)
photo = PhotoImage(file="1.png")
image_lable.pack()
"""

#for jpg images follow his format
image = Image.open("1.jpg")
photo = ImageTk.PhotoImage(image)
image_lable = Label(image=photo)
image_lable.pack()

root.mainloop()
