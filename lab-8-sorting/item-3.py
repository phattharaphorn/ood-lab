def selection_sort(l: list, i: int = 0) -> list:
    if len(l) - 1 == i:
        return
    max_i = l.index(max(l[:len(l) - i - 1]))
    cur_i = len(l) - i - 1
    if  max_i != cur_i:
        if l[max_i] > l[cur_i]:
            l[max_i], l[cur_i] = l[cur_i], l[max_i]
        selection_sort(l, i + 1 )
    return l

def combi(lst: list, n: int) -> list:
    if n == 0:
        return [[]]
    l =[]
    for i in range(0, len(lst)):         
        m = lst[i]
        remLst = lst[i + 1:]
        remainlst_combo = combi(remLst, n-1)
        for p in remainlst_combo:
             l.append([m, *p])     
    return l

def sum_list(l: list) -> int:
    sum = 0
    for i in range(len(l)):
        sum += l[i]
    return sum

def valid_combi(l: list, key: int) -> list:
    l_sum = list()
    for i in l:
        sum = sum_list(i)
        if sum == key:
            l_sum.append(i)
    return l_sum

inp = input("Enter Input : ").split('/')
l = selection_sort([int(i) for i in inp[1].split()])
l_valid = list()
for i in range(1,len(l)+1):
        l_valid += valid_combi(combi(l,i),int(inp[0]))
print(* l_valid,sep = '\n') if l_valid else print("No Subset") 
