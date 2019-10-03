num=int(input())
arrays=[]
for i in range(num):
    array=list(map(int,input().strip().split()))
    arrays.append(array)

for i in arrays:
    a,b,c=i[0],i[1],i[2]
    print((a*b)%c)
