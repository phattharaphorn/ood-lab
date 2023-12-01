class Queue :

    def __init__(self, list = None):
        if list == None :
            self.items = []
        else :
            self.items = list
        self.time = 0

    def isEmpty(self) :
        return self.items == []

    def enQueue(self, i) :
        self.items.append(i)

    def deQueue(self):
        if not self.isEmpty() : return self.items.pop(0)
        else : return -1

    def size(self) :
        return len(self.items)

    def __str__(self) :
        s = str(self.items)
        return s

def encodemsg(str, num) :

    lowercase = False
    for i in range(str.size()):
        if str.items[0] != str.items[0].lower() :
            str.items[0] = str.items[0].lower()
            lowercase = True
        str.items[0] = chr(ord(str.items[0]) + num.items[0])
        if ord(str.items[0]) > 122 :
            str.items[0] = chr(ord(str.items[0]) - 26)
        if lowercase :
            str.items[0] = str.items[0].upper()
            lowercase = False
        str.enQueue(str.deQueue())
        num.enQueue(num.deQueue())
    
    while Default_num != num.items :
        num.enQueue(num.deQueue())
    print("Encode message is : ",str.items)
        
def decodemsg(str, num) :
    
    lowercase = False
    for i in range(str.size()):
        if str.items[0] != str.items[0].lower() :
            str.items[0] = str.items[0].lower()
            lowercase = True
        str.items[0] = chr(ord(str.items[0]) - num.items[0])
        if ord(str.items[0]) < 97 :
            str.items[0] = chr(ord(str.items[0]) + 26)
        if lowercase :
            str.items[0] = str.items[0].upper()
            lowercase = False
        str.enQueue(str.deQueue())
        num.enQueue(num.deQueue())
    
    print("Decode message is : ",str.items)

inp  = input("Enter String and Code : ").split(',')

q1 = Queue([x for x in inp[0] if x != ' '])
q2 = Queue(list(map(int, inp[1])))
Default_num = list(map(int, inp[1]))
encodemsg(q1, q2)
decodemsg(q1, q2)