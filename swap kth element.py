
no_of_testcases= int(input())
input_array=[]
kth_elements=[]

def logic(number,k):
    a= number[k-1]
    b=number[-k]
    number[-k]=a
    number[k-1]=b
    print(*number,sep=' ')

for i in range(no_of_testcases):
    kth_element= list(map(int,input().strip().split()))
    input_Array= list(map(int,input().strip().split()))
    input_array.append(input_Array)
    kth_elements.append(kth_element[1])

for i in range(len(input_array)):
    logic(input_array[i],kth_elements[i])



