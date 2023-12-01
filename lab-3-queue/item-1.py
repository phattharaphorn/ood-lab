class Queue :

    def __init__(self, list = None):
        if list == None :
            self.items = []
        else :
            self.items = list

    def isEmpty(self) :
        return self.items == []

    def enQueue(self, i) :
        self.items.append(i)

    def deQueue(self):
        if not self.isEmpty() : return self.items.pop(0) + " 0"
        else : return -1

    def size(self) :
        return len(self.items)

    def __str__(self) :
        s = ""
        if not self.isEmpty() : 
            for i in self.items :
                s += i + " "
        else :
            s = "Empty"
        return s

q = Queue()

inp = [x for x in input("Enter Input : ").replace(',', ' ').split()]

for i in range(len(inp)) :
    if inp[i] == 'E' :
        q.enQueue(inp[i+1])
        print(q.size())
    elif inp[i] == 'D' :
        print(q.deQueue())
        
print(q)