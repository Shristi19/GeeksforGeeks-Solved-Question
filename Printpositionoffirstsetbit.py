def logic(num):
    x=str(bin(num)[2:])
    x = x[::-1]
    if '1' in x:
        print(x.index('1')+1)
    else:
        print(0)

num=int(input())
number=[]
for i in range(num):
    number.append(int(input()))
for i in range(num):
    logic(number[i])
