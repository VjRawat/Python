

def Addition(firstInput , secondInput):
    return firstInput + secondInput
    

def Subtraction(firstInput , secondInput):
    return firstInput - secondInput
      
def Division(firstInput , secondInput):
    return (firstInput/secondInput)

def Multiplication(firstInput , secondInput):
    return (firstInput*secondInput)


print("Mathematical Options")
print("A for Addition")
print("S for Subtraction")
print("D for Division")
print("M for Multiplication")

choice = input("Enter choice(A/S/D/M):")

try:
    firstInput = float(input("Enter the first value : "))
    secondInput = float(input("Enter the second value : "))

except ValueError:
    print("Enter the correct values.")

if choice == 'A':
    print("The sum of two number is: ", Addition(firstInput, secondInput))

elif choice == 'S':
    print("The sub of two number is: ", Subtraction(firstInput, secondInput))
        
elif choice == 'D':
    print("The div of two number is: ", Division(firstInput, secondInput))
    
elif choice == 'M':
    print("The Multi of two number is: ", Multiplication(firstInput, secondInput))

else:
    print("Invalid Input.")


