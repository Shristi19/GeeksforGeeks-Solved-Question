

number_of_testcases= int(input())
arrays=[]
k=[]
for i in range(number_of_testcases):
    lent=input()
    array=list(map(int,input().strip().split()))
    k_element=int(input())
    arrays.append(array)
    k.append(k_element)

for i in range(len(arrays)):
    arrays[i].sort()
    print(arrays[i][k[i]-1])
