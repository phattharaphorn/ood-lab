class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, str(self.tail.value) + " "
        while cur.previous != None:
            s += str(cur.previous.value) + " "
            cur = cur.previous
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        newNode = Node(item)
        cur = self.head
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            while cur != None:
                cur = cur.next
            cur.next = newNode
            newNode.previous = cur
            self.tail = newNode

    def addHead(self, item):
        newNode = Node(item)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            self.head.previous = newNode
            newNode.next = self.head
            self.head = newNode

    def insert(self, pos, item):
        newNode = Node(item)
        if self.isEmpty():
                self.head = newNode
                self.tail = newNode
        elif pos == 0:
                self.head.previous = newNode
                newNode.next = self.head
                self.head = newNode   
        else:
            cur_idx = 0
            while cur_idx != pos-1:
                cur = cur.next
                cur_idx += 1
            curNext = cur.next
            curNext.previous = None
            cur.next = newNode
            newNode.next = curNext
            newNode.previous = cur
        
    def search(self, item):
        cur = self.head
        if not cur != None:
            if cur.data == item:
                return 'Found'
            else:
                cur = cur.next
        else:
            return 'Not Found'

    def index(self, item):
        s = self.head
        idx = 0
        while s != None:
            if s.data == item:
                return idx
            s = s.next
            idx += 1
        return -1

    def size(self):
        s = self.head
        si = 0
        while s != None:
            s = s.next
            si += 1
        return si

    def pop(self, pos):
        if pos == 0:
            if self.isEmpty():
                self.head = None
                self.tail = None
            else:
                cur = self.head
                cur.next.previous = None
                self.head = self.head.next
                cur.next = None
        elif pos == self.size-1:
            cur = self.tail
            self.tail = self.tail.previous
            cur.previous = None
            self.tail.next = None
        else:
            cur = self.head
            cur_idx = 0
            while cur_idx < pos-1:
                cur = cur.next
                cur_idx += 1
            curNext = cur.next
            cur.next = curNext.next
            cur.next.previous = cur
            curNext.next = None
            curNext.previous = None
        self.size -= 1

L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
    elif i[:2] == "IS":
        data = i[3:].split()
        L.insert(int(data[0]), data[1])
print("Linked List :", L)
print("Linked List Reverse :", L.reverse())