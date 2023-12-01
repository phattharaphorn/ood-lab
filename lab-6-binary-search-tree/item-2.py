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
    
    def pre (self,node):
        print(node,end =' ')
        if node.left is not None:
            self.pre(node.left)
        if node.right is not None:
            self.pre(node.right)
    
    def inor (self,node):
        if node.left is not None:
            self.inor(node.left)
        print(node,end =' ')
        if node.right is not None:
            self.inor(node.right)
    
    def post (self,node):  
        if node.left is not None:
            self.post(node.left)
        if node.right is not None:
            self.post(node.right)
        print(node,end=' ')

    def Breadth(self,node):
        q = [node]
        while len(q) != 0:
            temp = q.pop(0)
            print(temp,end=' ')
            if temp.left is not None:
                q.append(temp.left)
            if temp.right is not None:
                q.append(temp.right)
T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
root = T.root 
for i in inp:
    root = T.insert(i,root)
print("Preorder : ",end = '')
T.pre(root)
print("\nInorder : ",end = '')
T.inor(root)
print("\nPostorder : ",end = '')
T.post(root)
print("\nBreadth : ",end = '')
T.Breadth(root)