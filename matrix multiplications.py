def logic(array):
    if len(array)%2==0:
        middle1=len(array)//2
        middle2=(len(array)//2)+1
        middle=(middle1+middle2)//2
    else :
        middle= len(array)//2

    left_Array=array[0:middle]
    right_Array=array[middle:len(array)]

    result= sum(left_Array)* sum(right_Array)
    print(result)


number_of_testcases=int(input())
for i in range(number_of_testcases):
    len_array=int(input())
    array= list(map(int,input().strip().split()))
    logic(array)
