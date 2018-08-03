import tkinter

addition = tkinter.Tk()

addition.title("Addition")

mainLabel = tkinter.Label(addition, text="ADDITION", fg="#2b5f7b")
mainLabel.config(font=("Arial", 30))
mainLabel.pack()

Subtitle = tkinter.Label(addition, text="Add values to perform Addition", fg="#1a303c")
Subtitle.config(font=("TimesInRoman", 20))
Subtitle.pack()

firstNumber = tkinter.Label(addition, text="First Name")
firstNumber.pack()

firstNumberValue = tkinter.Entry(addition)
firstNumberValue.pack()

secondNumber = tkinter.Label(addition, text="Last Name")
secondNumber.pack()

secondNumberValue = tkinter.Entry(addition)
secondNumberValue.pack()

def perfromAddition():
    firstNumber = int(firstNumberValue.get())
    secondNumber = int(secondNumberValue.get())

    result = firstNumber + secondNumber
    print("Result of addition is: ", result)

SubmitBtn = tkinter.Button(addition, text="Submit", command=perfromAddition)
SubmitBtn.pack()

addition.mainloop()
