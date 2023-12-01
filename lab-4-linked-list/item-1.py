class Node:
    def __init__(self,data):
        self.next = None
        self.data = data

class LinkedList:
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
                s += "->"
        return s

    def isEmpty(self):
        return self.size == 0

    def append(self, data):
        newNode = Node(data)
        if self.isEmpty(): 
            self.head = newNode
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = newNode
        self.size += 1

    def insert(self, index, data): 
        newNode = Node(data)
        
        if self.isEmpty():
            self.head = newNode
        elif index == 0:
            newNode.next = self.head
            self.head = newNode
        else:
            cur = self.head
            cur_idx = 0
            while cur_idx < index-1:
                cur_idx+=1
                cur = cur.next
            newNode = cur.next
            cur.next = newNode
        self.size += 1

    def remove(self,index):
        if not self.isEmpty():
            if index == 0:
                cur = self.head
                if cur.next!=None:
                    cur = cur.next
                self.head.next = None
                self.head = cur
            else:
                cur_idx = 0
                cur = self.head
                while cur_idx != index-1:
                    cur = cur.next
                    cur_idx += 1
                curNext = cur.next
                cur.next = curNext.next
                curNext.next = None
            self.size -= 1