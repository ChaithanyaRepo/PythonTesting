# Inheritance method in the python
from pythonBasic.oops import Calculator


class ChildCalculator(Calculator):
    num2 = 200

    # Parent constructor should call from child constructor if it is not a default constructor
    def __init__(self):
        # Invoking parent constructor
        Calculator.__init__(self, 10, 12)

    def getCompleteData(self):
        return self.num2 + self.num + self.Summation()


obj = ChildCalculator()
print(obj.getCompleteData())
