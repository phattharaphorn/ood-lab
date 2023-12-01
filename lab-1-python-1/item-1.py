print("*** Election ***")
num = int(input("Enter a number of voter(s) : "))
max = 0
y = 0
check = False
std = list(map(int,input().split()))
for i in std:
    x = std.count(i)
    if x > max and i > 0 and i <= 20:
        y = i
        max = x
        
    if i <= 20 and i > 0:
        check = True
        
if check == True:
    print(y)
else:
    print("*** No Candidate Wins ***")