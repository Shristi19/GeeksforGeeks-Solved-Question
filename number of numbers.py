number_of_testcases=int(input())
array_sizes=[]
arrays=[]
integer_count_for=[]


def logic(array,integer_digit):
    dict={}
    for i in array:
        temp=[int(j) for j in str(i)]
        for i in temp:
            if i in dict:
                dict[i]=dict[i]+1
            else:
                dict[i]=1
    result=dict[integer_digit]
    return result

for i in range(number_of_testcases):
    array_size=int(input())
    array=input().split()
    array=list(map(int,array))
    integer_count=int(input())
    array_sizes.append(array_size)
    arrays.append(array)
    integer_count_for.append(integer_count)

for i in range(number_of_testcases):
    print(logic(arrays[i],integer_count_for[i]))


