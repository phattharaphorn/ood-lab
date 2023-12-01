class Stack :
    def __init__(self, list = None) :
        if list == None:
            self.items = []
        else :
            self.items = list

    def isEmpty(self) :
        return self.items == []

    def size(self) :
        return len(self.items)
    
    def push(self, i) :
        self.items.append(i)
        return "Add = " + i

    def pop(self) :
        if not self.isEmpty() :
            return "Pop = " + self.items.pop() 
        else :
            return "-1"

    def peek(self):
        if not self.isEmpty() :
            return self.items[-1]

    def delete(self, num) :
        temp = Stack()
        if self.isEmpty() : print(-1)
        for item in self.items :
            if item == num : 
                temp.push(num) 
        self.items = [x for x in self.items if x != num]
        while not temp.isEmpty() :
            print("Delete = " + temp.peek())
            temp.pop()
            
    def lessThan_delete(self, num) :
        temp = Stack()
        if self.isEmpty() : print("-1")
        for item in self.items :
            if int(item) < int(num) : 
                temp.push(item) 
        
        self.items = [x for x in self.items if int(x) >= int(num)]
        while not temp.isEmpty() :
            print("Delete = {} Because {} is less than {}".format(temp.peek(),temp.peek(), num))
            temp.pop()

    def moreThan_delete(self, num) :
        temp = Stack()
        if self.isEmpty() : print("-1")
        for item in self.items :
            if item > num : 
                temp.push(item) 
        self.items = [x for x in self.items if x <= num]
        while not temp.isEmpty() :
            print("Delete = {} Because {} is more than {}".format(temp.peek(),temp.peek(), num))
            temp.pop()
        
    def __str__(self) :
        int_items = list(map(int, self.items))
        s = "Value in Stack = " + str(int_items)
        return s

stack = Stack()
list_input = [x for x in input("Enter Input : ").replace(',', ' ').split()]

for i in range(len(list_input)) :
    if list_input[i] == 'A' :
        print(stack.push(list_input[i + 1]))
    elif list_input[i] == 'P' :
        print(stack.pop())
    elif list_input[i] == 'D' :
        stack.delete(list_input[i + 1])
    elif list_input[i] == 'LD' :
        stack.lessThan_delete(list_input[i+1])
    elif list_input[i] == 'MD' :
        stack.moreThan_delete(list_input[i + 1])

print(stack)