'''
Given an array A containing a random permutation of distinct integers 
from 1 to N and a non-negative integer B representing the allowed number 
of swaps, the task is to find the largest possible permutation achievable 
after performing at most B swaps on the array elements.

Example:

Input: A = [1, 3, 2], B = 1
Output: [3, 1, 2]
'''


def largestPermutation(A,swaps):
    d = {}
    max = len(A)
    for i,j in enumerate(A):
        d[j] = i
    i = 0
    while(i<len(A) and swaps):
        j = d[max]
        if i != j:
            swaps-=1
            A[i],A[j] = A[j],A[i]
            d[A[i]],d[A[j]] = d[A[j]],d[A[i]]
        i+=1
        max-=1
            
        
    # print(d)
    return A
    
# Test cases
print(largestPermutation([1, 3, 2], 1))  # Output: [3, 1, 2]
print(largestPermutation([4, 2, 1, 3], 2))  # Output: [4, 3, 1, 2]
print(largestPermutation([5, 3, 2, 4, 1], 3))  # Output: [5, 4, 3, 2, 1]
print(largestPermutation([1], 0))  # Output: [1]
