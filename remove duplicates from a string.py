def logic(strin):
    dict={}
    for i in strin:
        if i in dict:
            dict[i]=dict[i]+1
        else:
            dict[i]=1
    result=[]
    for i in strin:
        if dict[i]==0:
            flag=0
        else:
            result.append(i)
            dict[i]=0

    print(''.join(result))



num=int(input())
arrays=[]
for i in range(num):
    array=input()
    arrays.append(array)

for i in arrays:
    logic(i)



