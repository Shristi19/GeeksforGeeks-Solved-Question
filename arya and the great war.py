def logic(number):
    bin1=str(bin(number))
    print(bin1.count('1'))




num=int(input())
numbers=[]
for i in range(num):
    number=int(input())
    numbers.append(number)
for i in range(num):
    logic(numbers[i])
