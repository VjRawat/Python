class SampleData:
    name = ""
    age = 0
    phone =0


    def __init__(self, name, age, phone):
        self.name = name
        self.age = age
        self.phone = phone

    def displayData(self):
        print("Name is: ", self.name)
        print("Age is: ", self.age)
        print("Phone is: ", self.phone)


#obj=SampleData("Vijay", 21, 1234)

# obj.displayData

#print("Name is :", obj.name)
#print("Age is: ", obj.age)
#print("phone is: ", obj.phone)

objList = []

obj  = SampleData("Vijay", 21, 7895)
obj1 = SampleData("Ankit", 21, 7854)
obj2 = SampleData("Ranu", 21, 3242)

objList.append(obj)
objList.append(obj1)
objList.append(obj2)

for item in objList:
    print("Name is :", obj.name)
    print("Age is: ", obj.age)
    print("phone is: ", obj.phone)
