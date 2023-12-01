class Stack():

    def __init__(self, ls = None):
        if ls == None:
            self.items = []
        else :
            self.items = ls

    def push(self,i):
        self.items.append(i)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)
    
def postFixeval(st):

    def popValue():
        x = s.pop()
        y = s.pop()
        return x, y

    s = Stack()

    for i in st :
        if i == '/' :
            x, y = popValue()
            s.push(y/x)
        elif i == '*' :
            x, y = popValue()
            s.push(y*x)
        elif i == '+' :
            x, y = popValue()
            s.push(y+x)
        elif i == '-' :
            x, y = popValue()
            s.push(y-x)
        else :
            s.push(int(i))

    return s.pop()

print(" ***Postfix expression calcuation***")
token = list(input("Enter Postfix expression : ").split())
print("Answer : ",'{:.2f}'.format(postFixeval(token)))