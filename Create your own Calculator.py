import numpy as np
import math
def logic(d,d1,d2,d3):
    detd=np.linalg.det(d)
    det1=np.linalg.det(d1)
    det2=np.linalg.det(d2)
    det3=np.linalg.det(d3)
    if detd!=0:
        print(math.floor(det1/detd),math.floor(det2/detd),math.floor(det3/detd))
    elif detd==0:
        if det1==0 and det3==0 and det2==0:
            print(1)
        elif det1!=0 or det2!=0 or det3!=0:
            print(0)


num=int(input())
d1s=[]
d2s=[]
d3s=[]
ds=[]
for i in range(num):
    a=list(map(float,input().split()))
    b=list(map(float,input().split()))
    c=list(map(float,input().split()))
    d=np.array([a[0:3],b[0:3],c[0:3]])
    ds.append(d)
    d1=np.array([[a[3],a[1],a[2]],[b[3],b[1],b[2]],[c[3],c[1],c[2]]])
    d2=np.array([[a[0],a[3],a[2]],[b[0],b[3],b[2]],[c[0],c[3],c[2]]])
    d3=np.array([[a[0],a[1],a[3]],[b[0],b[1],b[3]],[c[0],c[1],c[3]]])
    d1s.append(d1)
    d2s.append(d2)
    d3s.append(d3)

for i in range(num):
    logic(ds[i],d1s[i],d2s[i],d3s[i])



