input= int(input())
count=0
num=1
while count!=input:
    stri=bin(num)[2:]
    if '11' not in stri:
        count+=1
    num+=1
print(stri)
