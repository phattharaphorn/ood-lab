class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data,node):
        if node is None:
            return Node(data)
        if data < node.data:
            node.left = self.insert(data,node.left)
        elif data > node.data:
            node.right = self.insert(data,node.right)
        return node

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1) 
    
    def Below(self,node,data):
        have = None
        if node != None:
            if self.Below(node.left,data) is not None:
                have = 0
            if node.data < data:
                print(node,end = ' ')
                have = 0
            if self.Below(node.right,data) is not None:
                have = 0
        return have
    
T = BST()
temp=input('Enter Input : ').split('|')
inp = [int(i) for i in temp[0].split()]
root = T.root 
for i in inp:
    root = T.insert(i,root)
T.printTree(root)
print("--------------------------------------------------")
print("Below",temp[1],": ",end = '')
if T.Below(root,int(temp[1])) is None:
    print("Not have")