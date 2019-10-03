num=int(input())
arrays=[]
for i in range(num):
    lent=input()
    array=list(input().strip().split())
    arrays.append(array)
for list1 in arrays:
    list1.sort()
    print(list1[0],list1[-1])
