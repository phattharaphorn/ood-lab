class Node:
    def __init__(self,data):
        self.next = None
        self.data = data

class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __str__(self):
        s = ""
        cur = self.head
        while cur != None:
            s += str(cur.data)
            cur = cur.next
            if cur != None:
                s+= "->"
        return s

    def isEmpty(self):
        return self.size == 0

    def append(self, data):
        newNode = Node(data)
        if self.isEmpty(): 
            self.head = newNode
        else:
            cur = self.head
            while cur.next!=None:
                cur = cur.next
            cur.next = newNode
        self.size += 1

    def insert(self, index, data): 
        newNode = Node(data)
        cur = self.head
        if self.isEmpty(): 
            self.head = newNode
        elif index == 0:
            newNode.next = self.head
            self.head = newNode
        else:
            cur_idx = 0
            while cur_idx < (index-1):
                cur = cur.next
                cur_idx += 1
            newNode.next = cur.next
            cur.next = newNode
            
        self.size += 1

l = SingleLinkedList()
inp = [i.strip() for i in input("Enter Input : ").split(",")]

if inp[0] != "":
    for ele in inp[0].split():
        l.append(ele)
    print(f"link list : {l}")
else: print("List is empty")

for ele in inp[1:]:
    ele = ele.split(":")
    index = int(ele[0])
    data = int(ele[1])
    if index >= 0 and index <= l.size:
        l.insert(int(ele[0]),int(ele[1]))
        print(f"index = {index} and data = {data}")
        print(f"link list : {l}")
    else:
        print("Data cannot be added")
