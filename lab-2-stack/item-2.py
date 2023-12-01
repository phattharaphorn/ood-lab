class Stack():

    def __init__(self, ls = None):
        if ls == None:
            self.items = []
        else :
            self.items = ls

    def isEmpty(self):
        return self.items == []

    def push(self,i):
        self.items.append(i)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()

    def clear(self):
        self.items.clear()

    def size(self):
        return len(self.items)

    def peek(self):
        if not self.isEmpty() : return self.items[-1]

def dec2bin(decnum):
    
    s = Stack()
    st = ""
    while decnum > 0 :
        x = decnum % 2
        s.push(x)
        decnum //= 2
    
    while not s.isEmpty():
        st += str(s.pop())
    return st

print(" ***Decimal to Binary use Stack***")
token = input("Enter decimal number : ")

print("Binary number : ",end='')
print(dec2bin(int(token)))