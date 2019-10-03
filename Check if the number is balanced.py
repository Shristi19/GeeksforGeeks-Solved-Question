def logic(number):
    le=list(map(int,number[:len(number)//2]))
    ri=list(map(int,number[len(number)//2+1:]))
    if sum(le)==sum(ri):
        print(1)
    else:
        print(0)

num=int(input())
arrays=[]
for i in range(num):
    array=input()
    arrays.append(array)
for i in arrays:
    logic(i)
