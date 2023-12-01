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
        if not self.isEmpty() : 
            temp = self.items.pop(0)
            print(temp[1])
        else : print("Empty")

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

def addToMainQ(id) :
    for i in range(len(member_list)) :
        if member_list[i][1] == id :
            if mainq.isEmpty() : 
                mainq.enQueue(member_list[i])
                break
            for j in range(mainq.size()) :
                if member_list[i][0] == mainq.items[j][0] and j + 1 == mainq.size():
                    mainq.enQueue(member_list[i])
                elif member_list[i][0] == mainq.items[j][0] and member_list[i][0] != mainq.items[j+1][0] and j + 1 != mainq.size():
                    mainq.items.insert(j+1, member_list[i])
                    break
                elif member_list[i][0] != mainq.items[j][0] and j + 1 == mainq.size():
                    mainq.enQueue(member_list[i])

command = Queue()
mainq = Queue()

inp = input("Enter Input : ").split('/')
inp2 = [x for x in inp[0].split(',')]
member_list = []

for item in inp2 :
    member_list.append(list(map(int, item.split())))
command.items = [x for x in inp[1].replace(',', ' ').split()]

for i in range(command.size()) :
    if command.items[i] == 'D' :
        mainq.deQueue() 
    elif command.items[i] == 'E' :
        addToMainQ(int(command.items[i+1]))