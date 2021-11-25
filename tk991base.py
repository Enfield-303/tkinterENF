from tkinter import *
from PIL import ImageTk,Image


root = Tk()
root.title('OOP')


def open():
	global my_img #need global
	top = Toplevel()
	top.title('My Second Window')
	my_img = ImageTk.PhotoImage(Image.open("murad.jpg"))
	my_label = Label(top, image=my_img).pack()
	btn2 = Button(top, text="close window", command=top.destroy).pack()



btn = Button(root, text="Open Second Window", command=open).pack()

btn3 = Button(root, text="exit", command=root.quit).pack()


mainloop()