def print_space(space):
    if (space == 0):
        return;
    print("_", end = "");
    print_space(space - 1);
 
def print_sharp(sharp):
    if (sharp == 0):
        return;    
    print("#", end = "");
    print_sharp(sharp - 1);
 
def Staircase(n, num):
    if (n == 0):
        return;
    print_space(n - 1);
    print_sharp(num - n + 1);
    print();
    Staircase(n - 1, num);

def Staircase_reverse(n, num) :
    if (n == num - 1):
        return;
    print_space(n + 1);
    print_sharp(num - n - 1);
    print();
    Staircase_reverse(n + 1, num);

count = -1
n = int(input("Enter Input : "))
if n == 0:
    print("Not Draw!")
elif n > 0:
    Staircase(n, n)
else :
    n = abs(n)
    Staircase_reverse(count, n)