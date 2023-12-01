def FindMax(inp):
    if len(inp) == 1:
        return inp[0]
    else:
        return max(inp[0],FindMax(inp[1::]))

inp = [int(i.strip()) for i in input("Enter Input : ").split()]
print(f"Max = {FindMax(inp)}")