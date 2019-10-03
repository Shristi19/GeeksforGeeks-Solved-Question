import string
import  random
input=input()
input=list(input)

for i in range(len(input)-1):
    if input[i]=='?':
        rand=random.choice(string.ascii_lowercase)
        x=input[i-1]
        y=input[i+1]
        while(rand==x or rand==y):
            rand=random.choice(string.ascii_lowercase)
        input[i]=rand

if input[len(input)-1]=='?':
    y=input[len(input)-2]
    rand=random.choice(string.ascii_lowercase)
    while(rand==y):
        rand=random.choice(string.ascii_lowercase)
    input[len(input)-1]=rand



print(''.join(input))
