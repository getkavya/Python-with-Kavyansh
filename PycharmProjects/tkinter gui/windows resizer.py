from tkinter import *

root = Tk()
root.geometry("450x450")
root.config(bg="light green")

def resize():
    width_value = width.get()
    height_value = height.get()
    root.geometry(f"{width_value}x{height_value}")

root.title("Window Resizer")
Label(text="Window Resizer", font="comicsansms 11 bold", pady=20).grid(column=2)

Label(text="Width: ", font="comicsansms 11").grid(row=1, column=1)
Label(text="Height: ", font="comicsansms 11").grid(row=2, column=1)

width = StringVar()
height = StringVar()

width_entry = Entry(root, textvariable=width).grid(row=1, column=2)
height_entry = Entry(root, textvariable=height).grid(row=2, column=2)

Button(text="Apply", command=resize, fg='red', pady=2, font="comicsansms 13").grid(column=2)

root.mainloop()

