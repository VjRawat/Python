##class student:
##    studentName = ""
##    studentAddress = ""
##
##    def __init__ (self, studentName, studentAddress):
##        print("Hello you are in class")
##        self.studentName = studentName
##        self.studentAddress = studentAddress
##        print(self.studentName, self.studentAddress)
##
##
##
##
##studentName = input("Enter the student's name.")
##studentAddress = input("Enter student's address.")
##obj = student(studentName, studentAddress)
##
##
##
##
##
##class student:
##    firstNumber = ""
##    secondNumber = ""
##
##    def __init__(self, firstNumber, secondNumber):
##        print("hello!")
##        self.firstNumber = firstNumber
##        self.SecondNumber = secondNumber
##        self.multiply()
##
##
##    def multiply(self):
##        print(firstNumber * secondNumber)
##
##
##
##firstNumber = int(input("Enter the 1st number."))
##secondNumber = int(input("Enter the 2nd number."))
##obj = student(firstNumber, secondNumber)
##


class student:
    firstNumber = 0
    secondNumber = 0

    def __init__(self, firstNumber, secondNumber):
        self.firstNumber = firstNumber
        self.secondNumber = secondNumber
        result = self.multiply()
        print(result)
        


    def multiply(self):
        result = self.firstNumber * self.secondNumber
        return result
       


firstNumber = int(input("Enter the 1st number."))
secondNumber = int(input("Enter the 2nd number."))
obj = student(firstNumber, secondNumber)
