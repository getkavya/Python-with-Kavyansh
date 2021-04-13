from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("233x600")
root.title("Restaurant Menu")


def order():
    tmsg.showinfo("Order", f"We have received your order for\n{var.get()}\n{var2.get()}\n{var3.get()}\nThanks for ordering")

var = StringVar()
var.set("starters")
var2 = StringVar()
var2.set("main course")
var3 = StringVar()
var3.set("dessert")

Label(root, text = "Starters",font="lucida 19 bold",
      justify=LEFT, padx=14).pack(anchor="w")


radio = Radiobutton(root, text="Soup", padx=14, variable=var, value="Soup").pack(anchor="w")
radio = Radiobutton(root, text="Manchourian", padx=14, variable=var, value="Manchourian").pack(anchor="w")
radio = Radiobutton(root, text="Crispy Aloo", padx=14, variable=var, value="Crispy Aloo").pack(anchor="w")
radio = Radiobutton(root, text="Kebab", padx=14, variable=var, value="Kebab").pack(anchor="w")


Label(root, text = "Main Course",font="lucida 19 bold",
      justify=LEFT, padx=14).pack(anchor="w")

radio2 = Radiobutton(root, text="Butter Roti", padx=14, variable=var2, value="Butter Roti").pack(anchor="w")
radio2 = Radiobutton(root, text="Dal Tadka", padx=14, variable=var2, value="Dal Tadka").pack(anchor="w")
radio2 = Radiobutton(root, text="Paneer", padx=14, variable=var2, value="Paneer").pack(anchor="w")
radio2 = Radiobutton(root, text="Mix Veg", padx=14, variable=var2, value="Mix Veg").pack(anchor="w")


Label(root, text = "Dessert",font="lucida 19 bold",
      justify=LEFT, padx=14).pack(anchor="w")

radio3 = Radiobutton(root, text="Kulfi", padx=14, variable=var3, value="Kulfi").pack(anchor="w")
radio3 = Radiobutton(root, text="Ice-Cream", padx=14, variable=var3, value="Ice-Cream").pack(anchor="w")
radio3 = Radiobutton(root, text="Chocolate With Brownie", padx=14, variable=var3, value="Chocolate With Brownie").pack(anchor="w")
radio3 = Radiobutton(root, text="Choco Lava Cake", padx=14, variable=var3, value="Choco Lava Cake").pack(anchor="w")


Button(text="Order Now", command=order).pack()   


root.mainloop()
