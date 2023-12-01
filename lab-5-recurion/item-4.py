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

def move(n,from_rod, to_rod, aux_rod):
    if n == 1:
        print("move 1 from ",from_rod,"to",to_rod)
        change_pos(from_rod, to_rod)
        return
    move(n-1, from_rod, aux_rod, to_rod)
    print("move",n,"from ",from_rod,"to",to_rod)
    change_pos(from_rod, to_rod)
    move(n-1, aux_rod, to_rod, from_rod)

def Display(i, lstA, lstB, lstC) :
    a = lstA.items
    b = lstB.items
    c = lstC.items
    if i == -1 :
        return 
    if i < len(a):
        print(a[i], end="  ")
    else:
        print("|", end="  ")
    if i < len(b):
        print(b[i], end="  ")
    else:
        print("|", end="  ")
    if i < len(c):
        print(c[i])
    else:
        print("|")

    Display(i-1, listA, listB, listC)

def change_pos(form, des) :
    if form == 'A' : form = listA
    if form == 'B' : form = listB
    if form == 'C' : form = listC
    if des == 'A' : des = listA
    if des == 'B' : des = listB
    if des == 'C' : des = listC
    des.push(form.pop())
    Display(n, listA, listB, listC)

def initial_rod(n) :
    if n == 1:
        listA.push(n)
        return 0
    else :
        listA.push(n)
        initial_rod(n-1)

listA = Stack()
listB = Stack()
listC = Stack()

n = int(input("Enter Input : "))

initial_rod(n)

Display(n, listA, listB, listC)
move(n, 'A', 'C', 'B');