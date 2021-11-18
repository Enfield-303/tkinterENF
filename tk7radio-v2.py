from tkinter import *

root = Tk()
root.title('syedmurad.com')
root.geometry("300x300")

# ("text", "topping")
TOPPINGS = [
	("Pepperoni", "Pepperoni"),
	("Cheese", "Cheese"),
	("Mushroom", "Mushroom"),
	("Onion", "Onion"),
]

pizza = StringVar()
pizza.set("Pepperoni")

for text, topping in TOPPINGS:
	Radiobutton(root, text=text, variable=pizza, value=topping).pack(anchor=W)


def clicked(value):
	myLabel = Label(root, text=value)
	myLabel.pack()	


myButton = Button(root, text="Click Me!", command=lambda: clicked(pizza.get()))
myButton.pack()
mainloop()