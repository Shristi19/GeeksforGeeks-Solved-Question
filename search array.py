num=int(input())
arrays=[]
search=[]
for i in range(num):
    lenw=input()
    array=list(map(int,input().strip().split()))
    searc=int(input())
    arrays.append(array)
    search.append(searc)

for i in range(len(arrays)):
    if search[i] in arrays[i]:
        print(arrays[i].index(search[i]))
    else:
        print(-1)
