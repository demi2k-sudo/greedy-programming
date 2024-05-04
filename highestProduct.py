'''
Given an array of n integers, the problem asks you 
to find the highest product you can get by multiplying 
three integers from the array.
'''
def highestProduct(A):
    A.sort()
    
    hi3 =  A[-1]*A[-2]*A[-3]
    hi1lo2 =  A[-1]*A[0]*A[1]
    return max(hi3,hi1lo2)

print(highestProduct([1,0,2,3,4]))
print(highestProduct([-5,-2,-1,0,0,3,4,5]))
print(highestProduct([-5,-2,-1,0,0,1,1,5]))