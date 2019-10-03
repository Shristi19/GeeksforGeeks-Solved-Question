#code
def logic(arr,k):
    arr.sort()
    print(arr)
    rum=[]
    j=(k-1)
    for jk in range(len(arr)):
        if jk+j >= len(arr):
            break
        else:
            x=abs(arr[jk]-arr[jk+j])
            rum.append(x)
    print(min(rum))


arr=[]
k=[]
for i in range(int(input())):
    len1 = int(input())
    arr.append(list(map(int,input().strip().split())))
    k.append(int(input()))

for i in range(len(arr)):
    logic(arr[i],k[i])
