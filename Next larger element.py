
#Initial Template for Python 3
import atexit
import io
import sys
def nextLargerElement(arr,n):
    result=[]
    for i in range(n):
        next=-1
        for j in range(i+1,n):
            if arr[j]>arr[i]:
               next=arr[j]

        result.append(next)

    print(result)









_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER
@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        nextLargerElement(a,n)

''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
'''
Function Arguments : 
		@param  : arr(given array), n(size of array)
		@return : Print the Nge of corresponding Elements of array.
'''
