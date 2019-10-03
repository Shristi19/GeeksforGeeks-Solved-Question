number_of_testcases=int(input())
arrays=[]
for i in range(number_of_testcases):
    array=list(map(lambda x : int(x,2) , input().strip().split()))
    arrays.append(array)
for i in arrays:
    print(i[0]*i[1])

