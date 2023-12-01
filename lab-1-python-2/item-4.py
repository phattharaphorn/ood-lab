def weirdSubtract(n,k):
    for x in range(k) :
        if n%10 == 0 :
            n = n//10
        else :
            n = n-1
    return n

n,s = input("Enter num and sub : ").split()
print(weirdSubtract(int(n),int(s)))