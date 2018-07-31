class BaseClass:

    def __init__(self):
        print("This is base class.")

    def helloBaseClass(self):
        print("This is hello function inside the base class.")

class DerivedClass(BaseClass):

    def __init__(self):
        super(DerivedClass, self).helloBaseClass()
        print("This is derived class.")

obj = DerivedClass()
obj1 = BaseClass()


