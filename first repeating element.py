def logic(arr):
    dict={}
    for i in range(len(arr)):
        if arr[i] not in dict:
            dict[arr[i]]=i
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]==arr[j]:
                temp= arr[i]
                return dict[temp]+1
    else:
        return -1

no_of_tst=int(input())
arrays=[]
for i in range(no_of_tst):
    lene=input()
    array=list(map(int,input().strip().split()))
    arrays.append(array)
for i in arrays:
    print(logic(i))
