class Stack:

    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)
    
    def peek(self) :
        if self.isEmpty(): return None
        return int(self.items[-1])
    
    def pop(self):
        if self.isEmpty(): return None
        return self.items.pop()
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def push(self,i):
        return self.items.append(i)
    
    def __str__(self):
        s = ''
        for i in self.items:
            s += str(i) + ' '
        return s

S = Stack()
inp = input('Enter Input : ').split(',')
for ele in inp:
    ele = ele.split()
    if ele[0] == 'A':
        if S.isEmpty():
            S.push(int(ele[1]))
        else:
            while not S.isEmpty() and S.peek() <= int(ele[1]):
                S.pop()
            S.push(int(ele[1]))
    elif ele[0] == 'B':
        print(S.size())