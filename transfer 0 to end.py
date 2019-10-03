
def logic(i):
    count=i.count('0')
    i[:]=[j for j in i if j != '0']
    i.extend('0'*count)
    print(*i)


no_of_testcases = int(input())
number_Array=[]
for i in range(no_of_testcases):
    iw=input()
    numbers= list(input().strip().split())
    number_Array.append(numbers)

for i in number_Array:
    logic(i)
