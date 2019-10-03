number_testcases= int(input())
n, number_sum=input().split()
n= int(n)
for i in range(number_testcases):
    number_sum=int(number_sum)
    array=input().split()
    array=list(map(int,array))
    count=0
    for i in range(0,len(array)):
        for j in range(i+1,len(array)):
            if array[i]+array[j]==number_sum:
                count+=1
    print(count)


