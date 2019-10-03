def logic(arr):
    result=[]
    for i in range(len(arr)-1):
        if arr[i]> arr[i+1]:
            result.append(arr[i+1])
        else:
            result.append(-1)
    result.append(-1)
    print(*result)

num=int(input())
arra=[]
for i in range(num):
    le=input()
    arra.append(list(map(int,input().strip().split())))

for i in arra:
    logic(i)
