
def logic(li):
    li.sort()
    even=[]
    odd=[]
    for i in range(len(li)):
        if i%2==0:
            even.append(li[i])
        else:
            odd.append(li[i])
    even=int(''.join([str(i) for i in even]))
    odd=int(''.join([str(i) for i in odd]))
    print(even+odd)



inu=int(input())
numbers=[]
for i in range(inu):
    le=input()
    numbers.append(list(map(int,input().split())))
for i in numbers:
    logic(i)
