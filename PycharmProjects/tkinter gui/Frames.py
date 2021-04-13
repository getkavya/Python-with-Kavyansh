from tkinter import *
root = Tk()
root.geometry("600x400")
root.title("Learning Frames")

frame_1 = Frame(root, bg="grey", borderwidth=6, relief=SUNKEN)
frame_1.pack(side=LEFT, fill="y")

frame_2 = Frame(root, bg= "grey", borderwidth=8, relief=SUNKEN)
frame_2.pack(side=TOP, fill="x")

lable_frame = Label(frame_1, text="Tkinter Project - Text Editor", font="Helvetica 10 bold")
lable_frame.pack(pady=90)

lable_frame_2 = Label(frame_2, text="Welcome To PythonWithManan", font="Algerian", fg="red")
lable_frame_2.pack()

root.mainloop()