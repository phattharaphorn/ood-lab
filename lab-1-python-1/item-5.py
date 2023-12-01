import sys

print('*** Fun with Drawing ***')
num = int(input("Enter input : "))

if(num < 2):
  print('ERROR! you must to input more than 1')
  sys.exit()

for row in range((num*3) - 2):  
    for col in range(num + 1):  
        if ((col+row) == (num - 1)):
            print("*",end = "")
        else:  
            print(end = "-")  
    print()