import math
num=int(input())
number=[]
for i in range(num):
    number.append(int(input()))
for i in number:
    if i%10 in range(0,6):
        print(i-(i%10))
    else:
        print(i-(i%10)+10)
