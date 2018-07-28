firstNumber = int(input("Enter the first number: "))
secondNumber = int(input("Enter the second number: "))

if (firstNumber > secondNumber):
    for i in range (0,6):
        for j in range(1,i):
            print("*", end=" ")
elif(firstNumber < secondNumber):
    for k in range(0,6):
        for l in range(1,k):
            print("_", end=" ")
else:
    print("I don't know what's going on!")
    
                
                  
