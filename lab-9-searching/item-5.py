class hash:
     def __init__(self,size,maxCol,threshold):
          self.table = [None] * size
          self.size = size
          self.maxCol = maxCol
          self.threshold = threshold

     def insert(self,data):
          if self.isfull():
               print("****** Data over threshold - Rehash !!! ******")
               return False
          else:
               index = data % self.size

               if self.table[index] == None:
                    self.table[index] = data
               else:
                    col = 0
                    print(f'collision number {col+1} at {index}')
                    while True:
                         col += 1
                         newIndex = ( index + col * col ) % self.size
                         if self.maxCol <= col:
                              print("****** Max collision - Rehash !!! ******")
                              return False
                         if self.table[newIndex] == None:
                              self.table[newIndex] = data
                              break
                         print(f'collision number {col+1} at {newIndex}')
               return True

     def isfull(self):
          full = int(self.size * self.threshold / 100)
          count = 0
          for data in self.table:
               if data is not None:
                    count += 1
          if count >= full:
               return True
          return False

     def nextPrime(self,value):
          while value:
               value += 1
               for i in range(2,value):
                    if value % i == 0:
                         break
                    if i == value-1:
                         return value

     def printHashTable(self):
          for i in range(self.size):
               print(f'#{i+1}'+ " " * (7-len(str(i+1))) + f'{self.table[i]}')
          print("----------------------------------------")

print("***** Rehashing *****")
inp = input("Enter Input : ").split("/")

size, maxcol, threshold = map(int, inp[0].split())
data = list(map(int, inp[1].split()))
H = hash(size,maxcol,threshold)

print("Initial Table :")
H.printHashTable()

lastadd = -1
notall = True
while notall:
     for i in range(len(data)):
          if i >= lastadd + 1:
               print(f'Add : {data[i]}')
          if not H.insert(data[i]):
               H = hash(H.nextPrime(H.size * 2),maxcol,threshold)
               lastadd = i
               break
          else:
               if i >= lastadd:
                    H.printHashTable()
          if i == len(data) -1:
               notall = False