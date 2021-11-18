from tkinter import *

root = Tk()

e = Entry(root, width=30, font=('Helvetica', 16))
e.pack() 
e.get # used in fn
e.insert(0, "What is Your Name: ")

def myClick():
	hello = "Hello " + e.get()
	myLabel = Label(root, text=hello)
	# e.delete(0, 'end')
	myLabel.pack()


myButton = Button(root, text="Enter", command=myClick)
myButton.pack()



root.mainloop()

