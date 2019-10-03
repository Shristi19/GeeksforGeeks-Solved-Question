import math
no_of_testcases = int(input())
number_Array=[]
for i in range(no_of_testcases):
    numbers= int(input())
    number_Array.append(numbers)


for i in number_Array:
    if divisors(number) < 2*number:
        print(1)
    else:
        print(0)



def divisors(number):
    result_list=[]
    i=1
    while i <= math.sqrt(number):
        if number%i==0:
            if number/i == i:
                result_list.append(i)
            else:
                result_list.append(i)
                result_list.append(number/i)
        i+=1

    return sum(result_list)




