import itertools
def logic(i):
    x=list(itertools.combinations(i,2))
    result=[]

    for i in x:
        local=0
        a=str(bin(i[0])[2:])
        b=str(bin(i[1])[2:])
        if len(a) > len(b):
            b=b.zfill(len(a))
        elif len(b) > len(a):
            a=a.zfill(len(b))
        for i in range(len(a)):
            if a[i]!= b[i]:
                local=local+1
        result.append(local)
    print(sum(result))



num=int(input())
numbers=[]
for i in range(num):
    lrn=input()
    numbers.append(list(map(int,input().split())))


for i in numbers:
    logic(i)
