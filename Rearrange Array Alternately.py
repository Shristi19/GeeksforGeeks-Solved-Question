def logic(arr):
    result=[0]*len(arr)
    if len(arr)%2!= 0:
        j=1
        a=arr[0:int(len(arr)/2)]
        b=arr[int(len(arr)/2)+1:]
        c=arr[int(len(arr)/2)]
        j=1
        print(a,b)
        for i in range(0,len(a)):
            result[j]=a[i]
            j=j+2
        j=0
        for k in range(len(b)-1,-1,-1):
            print(b[k])
            result[j]=b[k]
            j+=2
        result[len(arr)-1]=c
        print(result)
    else:
        j=0
        a=arr[:int(len(arr)/2)]
        b=arr[int(len(arr)/2):]
        for i in range(0,len(a)):
            result[j]=a[i]
            j=j+2
        j=0
        for k in range(len(b)-1,-1,-1):
            print(b[k])
            result[j]=b[k]
            j+=2
        print(result)





num=int(input())
arra=[]
for i in range(num):
    len1=int(input())
    arra.append(list(input().split()))


for i in arra:
    logic(i)
