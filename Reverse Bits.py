




num=int(input())
number=[]
for i in range(num):
    number.append(int(input()))

for i in number:
    strbinary=str(bin(i))[2:]
    rev=strbinary[::-1]
    print(int(rev,2))

