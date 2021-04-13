from tkinter import *
root = Tk()
root.geometry("600x400")
root.title("My GUI with harry")

#Lable Options
"""
text = adds text to GUI
bd/bg = background
fg = foreground
font = sets the font 1 - font = ("style", size, "bold") 2 - font("style size bold")
padx = x padding
pady = y padding
relief = border stiling - Sunken, Raised, groove, Ridge
"""

title_lable = Label(text='''
Abdul Rashid Salim Salman Khan is an Indian 
\nfilm actor, producer, occasional playback singer and television personality. In a film career spanning 
\nalmost thirty years, Khan has received numerous awards, including two National Film Awards as a film 
\nproducer, and two Filmfare Awards for acting. He has a significant following in Asia and the Indian 
\ndiaspora worldwide, and is cited in the media as one of the most commercially successful actors of Indian 
\ncinema. According to the Forbes 2018 list of Top-Paid 100 Celebrity Entertainers in world, Khan was 
\nthe highest ranked Indian with 82nd rank with earnings of $37.7 million.''', 
bg= "blue", fg= "white", padx=35, pady= 80, font="comicsansms 11 bold", borderwidth=5 , relief=SUNKEN)
title_lable.pack(side="left", anchor="n", fill=Y)
root.mainloop()

# Important Pack options
"""
anchor = nw
side = top, bottom, left, right
fill
padx
pady
"""
