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
q2 = Queue()
x,y = input("Enter Input : ").split('/')
for ele in x.split():
    q.enQueue(ele)

for ele in y.split(","):
    ele = ele.split()
    if ele[0] == 'E':
        q2.enQueue(ele[1])
    elif ele[0] == 'D':
        q.deQueue()

for ele in q.items:
    if ele in q2.items:
        print("Duplicate")
        exit(0)
        
print("NO Duplicate")