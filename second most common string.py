def logic(strin):
    tu={}
    for i in strin:
        if i not in tu:
            tu[i]=strin.count(i)
    dict=list(zip(tu.keys(),tu.values()))
    sorte=sorted(dict,key=lambda x:x[1])
    print(sorte[-2][0])


num=int(input())
arrays=[]
for i in range(num):
    len2=input()
    array=list(input().strip().split())
    arrays.append(array)
for i in arrays:
    logic(i)
