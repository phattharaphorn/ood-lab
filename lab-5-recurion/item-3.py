def palin(char):
    if len(char) != 0:
        if char[0] == char[len(char)-1]:
                return palin(char[1:len(char)-1])
        else:
            return "is not palindrome"
    else:
        return "is palindrome" 

inp = input("Enter Input : ")
char = []
for i in inp:
    char.append(i)

print(f"'{inp}' {palin(char)}")