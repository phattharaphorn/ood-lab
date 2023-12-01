def insertion(l, sl = [], i = 0):
    if len(sl) == 0:sl = [l.pop(0)]
    if i == len(sl) or isLess(l,sl,i):
        sl.insert(i,l.pop(0))
        if len(l) == 0:
            return sl
        return insertion(l,sl)
    else:
        return insertion(l,sl,i+1)

def isLess(a,b,i):
    if a[0][1] < b[i][1]:return True
    if a[0][1] == b[i][1] and a[0][2] < b[i][2]:return True
    return False    
 
inp = [i.split(",") for i in input("Enter Input : ").split("/")]
print("== results ==")
for i in range(len(inp)):inp[i] = [inp[i][0],int(inp[i][1]) * 3 + int(inp[i][3]),int(inp[i][4]) - int(inp[i][5])]
for i in insertion(inp)[::-1]:
    print("[\'"+str(i[0])+"\', {\'points\':", str(i[1]) + "}, {\'gd\':", str(i[2]) + "}]")