for _ in range(int(input())):
    n = int(input())
    arr =input().split()
    for i in range(n):
        arr[i]=int(arr[i])

    missing=0
    repeating=-1
    for i in arr:
        if arr[abs(i)-1]<0 and repeating<0:
            repeating = abs(i)
        elif arr[abs(i)-1]>0:
            arr[abs(i)-1]*=-1
    #print(arr)
    for i in range(n):
        if arr[i]>0:
            print(repeating,i+1)
            break
