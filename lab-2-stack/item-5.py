class Stack():
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def pop(self):
        if self.isEmpty(): return None
        return self.items.pop()
    
    def push(self,value):
        return self.items.append(value)
    
    def __str__(self):
        s = ""
        for i in self.items:
            s += str(i) + ""
        return s

inp = input('Enter Input : ').split()
inp.reverse()
S = Stack()
x = 0
for i in inp:
    if S.size() < 2 or S.isEmpty():
        S.push(i)
    else:
        if S.items[-1] == S.items[-2] == i:
            S.pop()
            S.pop()
            x += 1
        else:
            S.push(i)

print(S.size())
if (S.size() > 0):
    print(S)
else:
    print("Empty")
if x >= 2:
    print(f"Combo : {x}!!!")