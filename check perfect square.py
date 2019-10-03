import math
num=int(input())
arrays=[]
for i in range(num):
    nuj=int(input())
    arrays.append(nuj)

for i in arrays:
    if math.sqrt(i).is_integer():
        print(1)
    else:
        print(0)
