def findmax(index,ls):
    if index == 0:
        return 0
    tempmax = findmax(index -1,ls)
    if ls[index] >= ls[tempmax]:
        return index
    return tempmax

def sort(index,ls):
    if index == 0:
        return 
    tempmax = findmax(index,ls)
    if tempmax != index:
        ls[index],ls[tempmax] = ls[tempmax],ls[index]
        print("swap",ls[tempmax],"<->",ls[index],":",ls)
    sort(index-1,ls)
    
inp = [int(e) for e in input("Enter Input : ").split()]
sort(len(inp) -1,inp)
print(inp)