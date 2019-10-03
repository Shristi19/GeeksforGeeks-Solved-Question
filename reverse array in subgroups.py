
import itertools

def logic(input_array,kth):
    list_of_list=[input_array[i:i+kth] for i in range(0,len(input_array),kth)]
    result=list(map(lambda x:x[::-1],list_of_list))

    print(*list((itertools.chain.from_iterable(result))))

no_of_testcases=int(input())
input_arrays=[]
kths=[]
for i in range(no_of_testcases):
    kth=list(map(int,input().strip().split()))
    input_array=list(map(int,input().strip().split()))
    input_arrays.append(input_array)
    kths.append(kth[1])

for i in range(len(input_arrays)):
    logic(input_arrays[i],kths[i])


