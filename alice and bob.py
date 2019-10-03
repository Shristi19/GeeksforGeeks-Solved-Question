import  itertools

a=1
b=3
c=1

list=list(itertools.product('abc',repeat=a+b+c))
for i in range(len(list)):
    list[i]=''.join(list[i])
print(list)
flag=0
out=''
for i in list:
    if i.count('a')==a and i.count('b')==b and i.count('c')==c:
        if 'aaa'not in i and 'bbb' not in i and 'ccc' not in i:
            print(i)
            flag=1
            out=i
            break

if flag==1:
    print(out)
else:
    print(-1)
