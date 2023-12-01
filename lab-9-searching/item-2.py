inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())), [int(i) for i in inp[1].split()]
for i in k:
    isF = True
    for j in sorted(arr):
        if i < j:
            print(j)
            isF = False
            break
    if isF:print("No First Greater Value")   