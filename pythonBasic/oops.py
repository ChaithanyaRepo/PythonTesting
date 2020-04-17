# Class :- userdefined prototype or datatype
class Calculator:
    # Class variables
    num = 100

    def __init__(self, a, b):
        # Instance variables
        self.firstnum = a
        self.secondnum = b
        print("Constructor of the class")

    def getData(self):
        print("First time using Method")

    def Summation(self):
        print("Summation using the variables")
        return self.firstnum + self.secondnum + obj.num + Calculator.num + self.num


# creating object for the class
obj = Calculator(2, 3)
print("Summation", obj.Summation())
obj.getData()

obj = Calculator(4, 5)
print("Summation", obj.Summation())



