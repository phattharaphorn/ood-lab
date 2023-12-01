"""
....#+++++
...##+###+
..###+###+
.####+###+
#####+++++
#####+++++
#+++#++++.
#+++#+++..
#+++#++...
#####+....

"""
num = int(input("Enter Input : "))
side_length = (num+2)*2
half_of_sidelength = side_length//2

for i in range(half_of_sidelength) :
    for j in range(side_length) :
        if j < half_of_sidelength :
            if half_of_sidelength - i - 1 <= j :
                print("#", end ='')
            else:
                print(".", end ='')
        elif j >= half_of_sidelength :
            if i == 0 or i == half_of_sidelength - 1 or j == half_of_sidelength or j == side_length - 1 :
                print("+", end ='')
            else :
                print("#", end ='')          
    print("")

for i in range(half_of_sidelength) :
    for j in range(side_length) :
        if j < half_of_sidelength :
            if i == 0 or i == half_of_sidelength - 1 or j == 0 or j == half_of_sidelength - 1 :
                print("#", end ='')
            else :
                print("+", end='')
        elif j >= half_of_sidelength :
            if side_length - i -1 >= j :
                print("+", end ='')
            else:
                print(".", end ='')                     
    print("")