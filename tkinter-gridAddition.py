import tkinter

gridAddition = tkinter.Tk()

gridAddition.title("Grid Addition")

headingLabel = tkinter.Label(gridAddition, text="Addition", bg="#d5e3eb", fg="#331063")
headingLabel.config(font=("Arial", 30))
headingLabel.grid(row=0, columnspan=3)

subHeading = tkinter.Label(gridAddition, text="Grid Addition", bg="#ccb3ee", fg="#165646")
subHeading.config(font=("Arial", 20))
subHeading.grid(row=1, columnspan=3)

firstNumber = tkinter.Label(gridAddition, text="Enter first Number")
firstNumber.grid(row=2, column=0)

firstNumberValue = tkinter.Entry(gridAddition)
firstNumberValue.grid(row=2, column=1)

secondNumber = tkinter.Label(gridAddition, text="Enter second Number")
secondNumber.grid(row=3, column=0)

secondNumberValue = tkinter.Entry(gridAddition)
secondNumberValue.grid(row=3, column=1)

def additionPerfom():

    firstNumber = int(firstNumberValue.get())
    secondNumber = int(secondNumberValue.get())

    result = firstNumber + secondNumber
    print("Addition is:", result)

submitBtn = tkinter.Button(gridAddition, text="Submit", command=additionPerfom, padx=5, pady=5)
submitBtn.config(cursor="gumby")
submitBtn.config(bg='dark green', fg='white')
submitBtn.config(font=('helvetica', 10, 'underline italic'))
submitBtn.grid(row=4, column=2)

gridAddition.mainloop()