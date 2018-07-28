#Exception handeling

def sum(userName, firstNumber ,secondNumber):
    thirdNumber = firstNumber + secondNumber
    print ("Hello" , userName, "the sum of" , firstNumber,
           "and", secondNumber, "is", thirdNumber)

userName = input("Enter the user name: ")

try:
    firstNumber = int(input("Enter the first number: "))
    secondNumber = int(input("Enter the second number: "))
    sum(userName, firstNumber, secondNumber)

except ValueError:
    print("Sorry, enter only integer value for numbers.")
