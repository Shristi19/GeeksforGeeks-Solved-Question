
def logic(li):
    li.sort()
    print(li)
    if len(li)<3:
        print(-1)
    else:
        print(max(li[-1]*li[-2]*li[-3],li[0]*li[1]*li[-1]))

inu=int(input())
numbers=[]
for i in range(inu):
    le=input()
    numbers.append(list(map(int,input().split())))
for i in numbers:
    logic(i)
