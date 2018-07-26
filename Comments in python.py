#variables in python are declared without datatype

##firstNumber = 20.14 #Variable-name = value
##secondNumber = 33.12

firstNumber = float(input("Enter the first Number."))
secondNumber = float(input("Enter the second Number."))

result = firstNumber + secondNumber

#we use print function to print any output
#to print any varible which is not of string datatype, use str() function
#to convert it only while displaying.

#print("sum of two number is:" + str(result))
##print("sum of two number i.e. %f and %f is: %f" % (firstNumber, secondNumber, result))
print("sum of two number i.e.", firstNumber,"and",secondNumber,"is:",result)
