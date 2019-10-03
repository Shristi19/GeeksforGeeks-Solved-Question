num=int(input())
number=[]
for i in range(num):
    number.append(input().strip())

for i in number:
    list=i.split('.')
    for i in range(len(list)):
        list[i]=list[i].lstrip('0')
    for i in range(len(list)):
        if list[i]=='':
            list[i]='0'
    print('.'.join(list))
