'''
Given an array of ratings ratings where ratings[i] 
represents the rating of the ith child, the task is 
to find the minimum number of candies that must be 
given to the children such that:

Every child receives at least one candy.
Children with higher ratings than their neighbors 
receive more candy.
'''

def getCandyPlan(A):
    
    data =[(i,j) for j,i in enumerate(A)]
    data.sort()
    
    candies = [1]*len(A)
    
    for _, i in data:
        # print(i)
        if i>0 and A[i]>A[i-1]:
            candies[i] = max(candies[i],candies[i-1]+1)
        if i<len(A)-1 and A[i]>A[i+1]:
            candies[i] = max(candies[i],candies[i+1]+1)
    
    return candies

print(getCandyPlan([1,3,7,1]))
print(getCandyPlan([1,2,7,4,3,3,1]))
    