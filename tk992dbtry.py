from tkinter import *
from PIL import ImageTk,Image
import sqlite3


root = Tk()
root.title('Syed Murad - database')
root.geometry("400x600")

# Databases

# Create a database or connect to one
conn = sqlite3.connect('C:/Users/ITC-LAB-T/Desktop/AP/address_book.db')

# Create cursor
c = conn.cursor()

# Create table

# c.execute("""CREATE TABLE addresses (
# 		first_name text,
# 		ast_name text,
# 		address text,
# 		city text
# 		)""")


# Create Submit Function For database
def submit():
	# Create a database or connect to one
	conn = sqlite3.connect('address_book.db')
	# Create cursor
	c = conn.cursor()

	# Insert Into Table
	c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city)",
			{
				'f_name': f_name.get(),
				'l_name': l_name.get(),
				'address': address.get(),
				'city': city.get()
			})


	#Commit Changes
	conn.commit()

	# Close Connection 
	conn.close()

	# Clear The Text Boxes
	f_name.delete(0, END)
	l_name.delete(0, END)
	address.delete(0, END)
	city.delete(0, END)


# Create Query Function
def query():
	# Create a database or connect to one
	conn = sqlite3.connect('address_book.db')
	# Create cursor
	c = conn.cursor()

	# Query the database
	c.execute("SELECT *, oid FROM addresses")
	records = c.fetchall()
	# print(records)

	# Loop Thru Results
	print_records = ''
	for record in records:
		print_records += str(record[0]) + " " + str(record[1]) + " " + str(record[2]) + " " + str(record[3]) + " " + "\n"
		# print_records += str(record[0]) + " " + str(record[1]) + " " + str(record[2]) + " " + str(record[3]) + " " + "\t ID" +str(record[4]) + "\n"


	query_label = Label(root, text=print_records)
	query_label.grid(row=12, column=0, columnspan=2)

	#Commit Changes
	conn.commit()

	# Close Connection 
	conn.close()

# Create Text Boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)
address = Entry(root, width=30)
address.grid(row=2, column=1)
city = Entry(root, width=30)
city.grid(row=3, column=1)



# Create Text Box Labels
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0, pady=(10, 0))
l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)
address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)
city_label = Label(root, text="City")
city_label.grid(row=3, column=0)





    # Create Submit Button
submit_btn = Button(root, text="Add Record To Database", command=submit)
submit_btn.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create a Query Button
query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=130)


#Commit Changes
conn.commit()

# Close Connection 
conn.close()

root.mainloop()
