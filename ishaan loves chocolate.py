number_of_testcases= int(input())
arrays=[]
array_size_S=[]
for i in range(number_of_testcases):
    array_size=int(input())
    array=input().split()
    array=list(map(int,array))
    array_size_S.append(array_size)
    arrays.append(array)

for i in range(number_of_testcases):
    if array_size_S[i]%2!=0:
        print(arrays[i][(array_size_S[i]//2+1)-1])

    else:
        mid1=array_size_S[i]//2
        mid2=array_size_S[i]+1//2
        if arrays[i][mid1-1] > arrays[i][mid2-1]:
            print(arrays[i][mid2-1])
        else:
            print(arrays[i][mid1-1])




