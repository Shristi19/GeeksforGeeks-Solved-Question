def logic(arr):
    count=0
    a=list(map(int,list(str(bin(arr[0])[2:]))))
    b=list(map(int,list(str(bin(arr[1])[2:]))))
    if len(a)<len(b):
        a=[0]*(len(b)-len(a))+a
    if len(b)<len(a):
        b=[0]*(len(a)-len(b))+b
    for i in range(len(a)):
        if a[i]!=b[i]:
            count+=1


    print(count)


num=int(input())
arra=[]
for i in range(num):
    arra.append(list(map(int,input().split())))


for i in arra:
    logic(i)
