'''
You have a group of mice and a set of holes, both placed along a straight line. 
Each mouse can move only one unit either to the left or right in one time unit. 
The task is to determine the minimum time it takes for all the mice to reach their 
respective holes.
'''

def timeTaken(mice, holes):
    mice.sort()
    holes.sort()
    time = 0
    for i,j in zip(mice,holes):
        currMouse = abs(i-j)
        time = max(currMouse,time)
    return time

print(timeTaken([3,2,-4],[0,-2,4]))
# Test cases
print(timeTaken([3, 2, -4], [0, -2, 4]))  
print(timeTaken([1, 2, 3], [1, 2, 3]))    
print(timeTaken([10, 20, 30], [5, 15, 25])) 
print(timeTaken([0, 0, 0], [0, 0, 0]))    
print(timeTaken([10, 20, 30], [20, 30, 45])) 
