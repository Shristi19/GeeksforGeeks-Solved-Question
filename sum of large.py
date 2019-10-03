def logic(x,y):
    if len(str(x+y))==len(str(x)):
        print(x+y)
    else:
        print(x)

num=int(input())
xs=[]
ys=[]
for i in range(num):
    x,y=list(map(int,input().strip().split()))
    xs.append(x)
    ys.append(y)
for i in range(num):
    logic(xs[i],ys[i])
