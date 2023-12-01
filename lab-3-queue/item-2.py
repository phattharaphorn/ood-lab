class  Queue():
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def enQueue(self,i):
        return self.items.append(i)
    
    def deQueue(self):
        return self.items.pop(0)
    
    def bottom(self):
        return self.items[-1]
    
    def front(self):
        return self.items[0]
    
    def __str__(self):
        s = ''
        for i in self.items:
            s = i + ''
        return s

q = Queue()
qEN = Queue()
inp = input("Enter Input : ").split(",")

for ele in inp:
    ele = ele.split()
    
    if ele[0] == 'ES':
        q.enQueue(ele[1])

    elif ele[0] == 'EN':
        qEN.enQueue(ele[1])

    elif ele[0] == 'D':
        if not qEN.isEmpty():
            for i in qEN.items:
                q.enQueue(i)
                qEN.deQueue()
        
        if q.isEmpty():
            print("Empty")
        else:
            print(q.front())
            q.deQueue()