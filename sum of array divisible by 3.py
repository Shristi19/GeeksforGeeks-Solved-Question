def logic(array):
    temp=list((''.join(array)))
    result=sum(list(map(int,temp)))
    if result%3 == 0:
        print(1)
    else:
        print(0)

number_of_testcases=int(input())
arrays=[]
for i in range(number_of_testcases):
    len=input()
    array=list(input().strip().split())
    arrays.append(array)

for i in arrays:
    logic(i)
