import tkinter as tk
from tkinter import *
from tkinter import ttk  #
import sqlite3

root = tk.Tk()
root.title("Management")

connection = sqlite3.connect('Management.db')

TABLE_NAME = "Management_table"
STUDENT_ID = "student_id"
STUDENT_NAME = "student_name"
STUDENT_COLLEGE = "student_college"
STUDENT_ADDRESS = "student_address"
STUDENT_PHONE = "student_phone"

connection.execute(" CREATE TABLE IF NOT EXISTs " + TABLE_NAME + " ( " + STUDENT_ID + " INTEGER PRIMARY KEY AUTOINCREMENT, "
                   + STUDENT_NAME + " TEXT, " + STUDENT_COLLEGE + " TEXT, " + STUDENT_ADDRESS + " TEXT, " + STUDENT_PHONE
                   + " INTEGER);")

appLabel = tk.Label(root, text="Student management system", fg="#5a990c", width=40)
appLabel.config(font=("sylfaen", 30))
appLabel.grid(row=0, columnspan=2, padx=(30,30), pady=(30,0))

class student:
    studentName = ""
    collegeName = ""
    phoneNumber = 0
    address = ""

    def __int__(self, studentName, collegeName, phoneNumber, address):
        self.studentName = studentName
        self.collegeName = collegeName
        self.phoneNumber = phoneNumber
        self.address =  address

nameLabel= tk.Label(root, text="Enter your name", width=40, anchor  ='w')\
        .grid(row=1,column=0, padx=(30, 0), pady=(30,0))
collegeLabel= tk.Label(root, text="Enter the college name", width=40, anchor= 'w')\
        .grid(row=2, column=0, padx=(30, 0), pady=(30,0))
phoneLabel = tk.Label(root, text="Enter the phone Number", width=40, anchor= 'w') \
        .grid(row=3, column=0, padx=(30, 0), pady=(30, 0))
addressLabel = tk.Label(root, text="Enter the address", width=40, anchor= 'w')\
        .grid(row=4, column=0, padx=(30, 0), pady=(30,0))

nameEntry=  Entry(root)
collegeEntry= Entry(root)
phoneEntry= Entry(root)
addressEntry= Entry(root)

nameEntry.grid(row=1, column=1, padx=(0,50), pady=(30, 20))
collegeEntry.grid(row=2, column=1, padx=(0,50), pady = 20)
phoneEntry.grid(row=3, column=1, padx=(0,50), pady = 20)
addressEntry.grid(row=4, column=1, padx=(0,50), pady = 20)

username = ""
collegeName = ""
phone = ""
address = ""
list = []

def takeNameInput():
    global nameEntry, collegeEntry, phoneEntry, addressEntry
    global username, collegeName, phone, address
    global list
    global TABLE_NAME, STUDENT_NAME, STUDENT_COLLEGE, STUDENT_ADDRESS, STUDENT_PHONE
    username = nameEntry.get()
    nameEntry.delete(0, END)
    collegeName = collegeEntry.get()
    collegeEntry.delete(0, END)
    phone = int(phoneEntry.get())
    phoneEntry.delete(0, END)
    address = addressEntry.get()
    addressEntry.delete(0, END)

    connection.execute("INSERT INTO " + TABLE_NAME + " ( " + STUDENT_NAME + ", " +
                       STUDENT_COLLEGE + ", " + STUDENT_ADDRESS + ", " +
                       STUDENT_PHONE + " ) VALUES ( '"
                       + username + "', '" + collegeName + "', '" +
                       address + "', " + str(phone) + " ); ")
    connection.commit()


def destroyRootWindow():
    root.destroy()

def printDetails():
    for singleItem in list:
        print("Student name is: %s\nCollege name is: %s\nPhone number is: %d\nAddress is: %s" %
              (singleItem.studentName, singleItem.collegeName, singleItem.phoneNumber, singleItem.address))
        print("****************************************")

button = tk.Button(root, text="Take input", command=takeNameInput)
button.grid(row=5, column=0, pady=30)

displayButton = tk.Button(root, text="Display result", command=destroyRootWindow)
displayButton.grid(row=5, column=1)

root.mainloop()

secondWindow = tk.Tk()

secondWindow.title("Display results")

appLabel = tk.Label(secondWindow, text="Student Management System", fg="#06a099", width=40)
appLabel.config(font=("Sylfaen", 30))
# appLabel.grid(row=0, columnspan=2, padx=(30,30), pady=(30, 0))
appLabel.pack()

tree = ttk.Treeview(secondWindow)
tree["columns"]=("one","two", "three", "four")
tree.column("one", width=200)
tree.column("two", width=200)
tree.column("three", width=200)
tree.column("four", width=200)
tree.heading("one", text="Student Name")
tree.heading("two", text="College Name")
tree.heading("three", text="Address")
tree.heading("four", text="Phone Number")


cursor = connection.execute("SELECT * FROM " + TABLE_NAME + " ;")
i = 0

for row in cursor:
    tree.insert('', i, text="Student " + str(row[0]),
                values=(row[1], row[2],
                        row[3], row[4]))
    i = i+1

# for singleItem in list:
    # tree.insert('', i, text="Student " + str(i+1),
    #             values=(singleItem.studentName, singleItem.collegeName,
    #                     singleItem.phoneNumber, singleItem.address))
    # i = i+1


tree.pack()

connection.close()

secondWindow.mainloop()







