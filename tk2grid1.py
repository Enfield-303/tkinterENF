from tkinter import *

root = Tk()

# Creating a Label Widget
myLabel1 = Label(root, text="Hello Class!")
myLabel2 = Label(root, text="My Name Is Syed Murad")

# Shoving it onto the screen or do it with .grid()

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=5)


root.mainloop()

