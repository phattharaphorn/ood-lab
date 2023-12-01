class Calculator :
    def __init__(self,num):
        self.num = num
    
    def __add__(self,y):
        add = self.num + y.num
        return add

    def __sub__(self,y):
        sub = self.num - y.num
        return sub

    def __mul__(self,y):
        mul = self.num * y.num
        return mul

    def __truediv__(self,y):
        truediv = self.num / y.num
        return truediv
    
x,y = input("Enter num1 num2 : ").split(",")
x,y = Calculator(int(x)),Calculator(int(y))
print(x + y, x - y, x * y, x / y, sep = "\n")