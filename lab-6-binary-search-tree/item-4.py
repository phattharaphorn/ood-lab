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

    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            cur = self.root
            while cur != None:
                if data >= cur.data:
                    if cur.right == None:
                        cur.right = Node(data)
                        break
                    cur = cur.right
                elif data < cur.data:
                    if cur.left == None:
                        cur.left = Node(data)
                        break
                    cur = cur.left
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def find(self, data):
        global k,num
        if data <= k:
            num += 1
        return num

T = BST()
list1 = []
num = 0
inp = input('Enter Input : ').split("/")
k = int(inp[1])
for i in inp[0].split():
    i = int(i)
    list1.append(i)
for i in list1:
    root = T.insert(i)
    T.find(i)

T.printTree(T.root)
print("--------------------------------------------------")
print(num)