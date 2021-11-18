from tkinter import *

root = Tk()

def myClick():
	myLabel = Label(root, text="Look! I clicked a Button!!") 
	myLabel.pack()

myButton = Button(root, text="Click Me!", command=myClick,  pady=20, bg="green") # fg="blue", bg="green"  # padx=60, pady=60
myButton.pack()



root.mainloop()

