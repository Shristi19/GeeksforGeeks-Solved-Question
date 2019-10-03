def logic(number1,number2):
    a=number1[0]
    b=number2[-1]
    number1[0]=b
    number2[-1]=a
    c=number1[-1]
    number1[-1]=number2[0]
    number2[0]=c
    print(''.join(number1)+' '+''.join(number2))
num=int(input())
strin1=[]
for i in range(num):
    strin1.append(list(input().split()))
for i in range(num):
    logic(list(strin1[i][0]),list(strin1[i][1]))
