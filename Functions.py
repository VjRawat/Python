#Create a function without parameters
def functionName ():
    print("Hello World")

functionName()




#create a function with parameters
def fucntionName(name):
    print("Hello!" + name)

fucntionName("Vijay")



#Create a function with parameters and return
def sum(firstNumber , secondNumber):
    thirdNumber = firstNumber + secondNumber
    return thirdNumber

result = sum(10, 20)
print(result)


#Create a function with the help of users input and parameters but not return value 
userName = input("Enter the user name: ")
firstNumber = int(input("Enter the first number: "))
secondNumber = int(input("Enter the second number: "))

def sum(userName, firstNumber ,secondNumber):
    thirdNumber = firstNumber + secondNumber
    print ("Hello" , userName, "the sum of" , firstNumber, "and", secondNumber, "is", thirdNumber)

sum(userName, firstNumber, secondNumber)
