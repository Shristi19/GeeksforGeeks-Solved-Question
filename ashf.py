#code
def logic(numb):
    sum=0
    for i in range(1,numb+1):
        sum=sum+(i+1)**2-((3*i)+1)+i

    print(sum)

number=[]
num_testcase=int(input())
for i in range(num_testcase):
    number.append(int(input()))
for numb in number:
    logic(numb)
