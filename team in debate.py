def logic(i):
    if i== 1:
        print(1)
    else:
        print(int(i/2))

num=int(input())
for i in range(num):
    numbers=[]
for i in range(num):
    numbers.append(int(input()))

for i in numbers:
    logic(i)
