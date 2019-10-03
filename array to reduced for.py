def logic(list1):
    temp={}
    list_new=[0]*(len(list1))
    for i in range(len(list1)):
        temp[list1[i]]=i
    list1.sort()
    count=0
    for i in list1:
        index=temp[i]
        list_new[index]=count
        count+=1
    print(*list_new)

no_of_testcases=int(input())
arrays=[]
for i in range(no_of_testcases):
    lent=input()
    array=list(map(int,input().strip().split()))
    arrays.append(array)

for i in arrays:
    logic(i)

