class BaseClass:
        firstNumber = 0
        secondNumber = 0
        result = 0

        def __init__(self, firstNumber, secondNumber):

            self.firstNumber = firstNumber
            self.secondNumber = secondNumber

        def sumOfTwoNumbers(self):
            self.result = self.firstNumber + self.secondNumber
            return self.result

class DerivedClass(BaseClass):                                                   # Inherit the Parent class(BaseClass) by child class(DerivedClass)

    def __init__(self, firstNumber, secondNumber):
        super(DerivedClass, self).__init__(firstNumber, secondNumber)             # super keyword called the parent class(BaseClass) constructor
        result = super(DerivedClass, self).sumOfTwoNumbers()
        print("Then sum of two numbers is: ",result)

        # print(result)
try:
    firstNumber = int(input("Enter your first Value: "))
    secondNumber = int(input("Enter yout second Value: "))
    obj = DerivedClass(secondNumber=secondNumber, firstNumber=firstNumber)

except ValueError:
        print("Sorry! Enter the integer Value only.")

