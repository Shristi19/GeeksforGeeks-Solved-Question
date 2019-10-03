def logic(a,b):
    if a%2==0 and b%2==0:
        print('EVEN')
    else:
        print('ODD')
num=int(input())
patt=[]
for i in range(num):
    LE=input()
    patt.append(input())

for i in range(num):
    a,b=patt[i].split('.')
    logic(int(a),int(b))
