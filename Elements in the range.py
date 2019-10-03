def logic(a,b,lis):
    flag=0
    range1=[i for i in range(a,b+1)]
    lis.sort()
    if lis.index(a):
        ind=lis.index(a)
        for i in range(ind,len(range1)):
            if lis[i] in range1:
                continue
            else:
                flag=1
                break
        if flag==1:
            print('No')
        else:
            print('Yes')
    else:
        print('No')

num=int(input())
aas=[]
bs=[]
nums=[]
for i in range(num):
    lena,a,b=input().split()
    aas.append(int(a))
    bs.append(int(b))
    nums.append(list(map(int,input().strip().split())))

for i in range(num):
    logic(aas[i],bs[i],nums[i])
