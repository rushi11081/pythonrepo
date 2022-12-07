from oops import Calc


class Child(Calc):
    num2 = 200

    def  __init__(self):
        print("he")


    def child1(self):
        print(Calc.num + self.num2)


obj = Child()
obj.child1()


str="rahulshettyacademy.com"
str1="com"
print(str)
print(str[0])
print(str[0:5])
print(str1 in str)
var=str.split(".")
print(var)
print(var[0])
