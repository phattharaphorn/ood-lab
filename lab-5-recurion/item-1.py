def fac(num):
    if num == 1:
        return num
    elif num == 0:
        return 0
    else:
        return num * fac(num-1)

inp = [i.strip() for i in input("Enter Input : ")]
num = int(inp[0])
print(fac(num))