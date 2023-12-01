def checkDrome(inp):
    ans = ""
    if inp[0] < inp[1]:
        ans = "Metadrome"
        for i in range(len(inp[:-1])):
            if inp[i] > inp[i+1] :
                print("Nondrome")
                exit()
            elif inp[i] == inp[i+1]:
                ans = "Plaindrome"
        print(ans)
    elif inp[0] > inp[1]:
        ans = "Katadrome"
        for i in range(len(inp[:-1])):
            if inp[i] < inp[i+1] :
                print("Nondrome")
                exit()
            elif inp[i] == inp[i+1]:
                ans = "Nialpdrome"
        print(ans)

arr =[* input("Enter Input : ")]
arr = list(map(int,arr))

if arr[0] == arr[1]:
    for i in range(len(arr[:-1])):
        if arr[i] != arr[i + 1]:
            checkDrome(arr)
    print("Repdrome")
else :
    checkDrome(arr)