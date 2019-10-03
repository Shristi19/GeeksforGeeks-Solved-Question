
def logic(number):
    a=int(((number*(number+1))/2)**2)
    sum=0
    for i in range(1,number+1):
        sum=i**2+sum
    print(a-sum)


num_of_testcases=int(input())
arrays=[]

for i in range(num_of_testcases):
    array=int(input())
    arrays.append(array)

for i in arrays:
    logic(i)
