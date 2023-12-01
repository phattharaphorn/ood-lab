class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class hash:
    def __init__(self,size,m):
        self.size = size
        self.table = [None for i in range(size)]
        self.maxCollision = m
    
    def isFull(self):
        for i in self.table:
            if i == None:return False
        return True
    
    def insert(self,key,data):
        if self.isFull():
            print("This table is full !!!!!!")
            exit()
        index = sum([ord(i) for i in key]) %self.size
        realIndex = index
        col = 0
        while self.table[index] != None:
            col += 1
            print("collision number",col,"at",index)
            if col == self.maxCollision:
                print("Max of collisionChain")
                break
            else:
                index = (realIndex + col ** 2) %self.size
        if self.table[index] == None:self.table[index] = str(Data(key,data))
    
    def printTable(self):
        for i in range(self.size):
            print("#" + str(i + 1) +"	",end = "")
            if self.table[i] == None:print(None)
            else:print(self.table[i])
        print("---------------------------")

print(" ***** Fun with hashing *****")
inp = input("Enter Input : ").split("/")
h = hash(int(inp[0].split()[0]),int(inp[0].split()[1]))
for i in inp[1].split(","):
    h.insert(i.split()[0],i.split()[1])
    h.printTable()