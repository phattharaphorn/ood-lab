class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.data) 

class BST:
    def __init__(self): 
        self.root = None
    
    def getMinNode(self,root):
        current = root
        while current.left:
            current = current.left
        return current

    def insert(self, val):  
        if self.root is None:
            self.root = Node(val)
        else:
            current = self.root
            while True:
                if val < current.data:
                    if not current.left:
                        current.left = Node(val)
                        break
                    current = current.left
                else:
                    if not current.right:
                        current.right = Node(val)
                        break
                    current = current.right
        return self.root

    def delete(self,r,data):
        parent = None
        current = r
        while current and current.data != data:
            parent = current

            if data < current.data:
                current = current.left
            else:
                current = current.right
        
        if current is None:
            print('Error! Not Found DATA')
            return r
        
        if current.left is None and current.right is None:
            if current != r:
                if parent.left == current:
                    parent.left = None
                else:
                    parent.right = None
            else:
                r = None
            
        elif current.left and current.right:
            successor = self.getMinNode(current.right)
            temp = successor.data
            self.delete(r,successor.data)
            current.data = temp
        
        else:
            if current.left:
                child = current.left
            else:
                child = current.right
            
            if not parent:
                r = child

            if child != r:
                if current == parent.left:
                    parent.left = child
                else:
                    parent.right = child
        return r
                
    def printTree90(self, node, level = 0):
        if node != None:
            self.printTree90(node.right, level + 1)
            print('     ' * level, node)
            self.printTree90(node.left, level + 1)

def findRank(node, value):
    global rank
    global ans
    global found
    if node == None:
        return
    findRank(node.left, value)
    rank += 1
    if node.data == value:
        if not found:
            ans = rank - 1
            return
    elif node.data > value:
        if not found:
            found = True
            ans = rank - 1
            return
    findRank(node.right, value)
    if not found:
        ans = rank

inp, val = input('Enter Input : ').split('/')
inpLis = [int(e) for e in inp.split()]
ans = 0
rank = 0
found = False
T = BST()
for data in inpLis:
    T.insert(data)
T.printTree90(T.root)
findRank(T.root, int(val))
print('--------------------------------------------------')
print('Rank of {0} : '.format(val) + str(ans))