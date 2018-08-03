import tkinter  # import tkinter package

top = tkinter.Tk()  # top is just a variable

top.title("Tkinter sample ")  # to set title of window

# using tkinter label
# first send window object, text to displayed
headingLabel = tkinter.Label(top, text="Hello Welcome to Tkinter", fg="#2b5f7b")
headingLabel.config(font=("Arial", 30))

# after that use pack or grid
headingLabel.pack()

bodyLabel = tkinter.Label(top, text="Vijay Rawat", bg="#fca99a")
bodyLabel.config(font=("Arial", 20))
bodyLabel.pack()

footerLabel = tkinter.Label(top, text="Hello Python", bg="#3b5461")
footerLabel.config(font=("TimesInRoman", 30))
footerLabel.pack()

nameValue = tkinter.Entry(top)  #
nameValue.pack()

def takeInput():
    print("Submitted")

SubmitBtn = tkinter.Button(top, text="Submit", command=takeInput)
SubmitBtn.pack()


top.mainloop()