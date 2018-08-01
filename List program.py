class SampleData:
        name = ""
        age = 0
        phone = 0

        def __init__(self, name, age, phone):
            self.name = name
            self.age = age
            self.phone = phone

        def displayData(self):
            print("Name is :", self.name)
            print("Age is: ", self.age)
            print("Phone is: ", self.phone)

objList = []

numberOfEnteries = int(input("Enter the number of enteries you want to make: "))

for i in range(0, numberOfEnteries):
    print("Enter the student details: ")
    name = input("Enter the sutdent name: ")
    age = int(input("Enter the age: "))
    phone = int(input("Enter the phone number: "))

    obj = SampleData(name, age, phone)
    objList.append(obj)
# obj  = SampleData("Vijay", 21, 7895)
# obj1 = SampleData("Ankit", 21, 7854)
# obj2 = SampleData("Ranu", 21,3242)
#
#
# objList.append(obj)
# objList.append(obj1)
# objList.append(obj2)

for item in objList:
    print("Name is :", item.name)
    print("Age is: ", item.age)
    print("phone is: ", item.phone)



