
def logic(arry1,arry2):
    temp=set(arry2)|set(arry1)
    print(len(temp))
arrys1=[]
arrys2=[]
no_of_testcases=int(input())
for i in range(no_of_testcases):
    len1=list(map(int,input().strip().split()))
    arry1=list(map(int,input().strip().split()))
    arry2=list(map(int,input().strip().split()))
    arrys1.append(arry1)
    arrys2.append(arry2)
for i in range(0,len(arrys1)):
    logic(arrys1[i],arrys2[i])


