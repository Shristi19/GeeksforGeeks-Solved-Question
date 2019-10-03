num=int(input())
arrays=[]
for i in range(num):
    lenw=input()
    array=list(map(int,input().strip().split()))
    arrays.append(array)

for i in range(len(arrays)):
    dict={}
    for item in arrays[i]:
        if item in dict:
            dict[item] = dict[item]+1
        else:
            dict[item]=1
    majo=-1
    for key,value in dict.items():
        if value > len(arrays[i])/2:
            majo=key
            break

    print(majo)

