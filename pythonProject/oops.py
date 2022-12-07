class Calc:
    num = 100

    def __init__(self, a, b):
        self.first = a
        self.second =b

    def mydata(self):
        print("mydatafunction")

    def add1(self):
        return self.first + self.second


obj = Calc(2, 3)
obj.mydata()
print(obj.add1())
print(obj.num)

obj1 = Calc(4, 5)
obj1.mydata()
print(obj1.add1())
print(obj1.num)
