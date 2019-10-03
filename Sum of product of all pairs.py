import itertools
def logic(li):
    final=[]
    for i in range(len(li)):
        for j in range(i+1,len(li)):
            final.append((li[i],li[j]))
    re=[i[0]*i[1] for i in final]
    print(sum(re))

inu=int(input())
numbers=[]
for i in range(inu):
    le=input()
    numbers.append(list(map(int,input().split())))
for i in numbers:
    logic(i)
