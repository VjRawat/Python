#not completed

def inputNumber(firstNumber):
    if(firstNumber == 1):
        for i in range(1,4):
            for j in range(1, i+1, +1):
               print(j, end=" ")
            print(" ")
    elif(firstNumber == 2):
        for k in range(0,4):
            for l in range(3, k, -1):
                print("*", end=" ")
            print(" ")
    else:
        print("Last one not possible :P .")
##        for m in range(0,4):
##            for n in range(3, i, -1):
##                print(n, end=" ")
##                for o in range(2, i
                

try:
    firstNumber = int(input("enter the number: "))
    inputNumber(firstNumber)

except ValueError:
    print("Sorry! , Enter the integer value only." )   
