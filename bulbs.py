'''
Given N bulbs, which are either on (represented by 1) 
or off (represented by 0). If you turn on the ith bulb, 
all the bulbs to the right of it will flip their state 
(turn on if off, turn off if on).

What to find

The problem asks you to find the minimum number of times 
you need to turn on a switch to turn all the bulbs on.

Constraints

There are between 1 and 100,000 bulbs (1 ≤ N ≤ 1e5).
Each bulb can only be on or off (A[i] = {0, 1}).
'''

def minSwitches(A):
    cost = 0
    for b in A:
        if cost%2 == 0:
            b = b 
        else:
            b = 1 if b == 0 else 0
        if b%2 == 1:
            continue
        else:
            cost+=1
    return cost
            
print(minSwitches([1, 0, 1, 1]))
print(minSwitches([1, 1, 1, 1]))
print(minSwitches([0]))
print(minSwitches([0, 1]))
print(minSwitches([1, 0, 0]))
print(minSwitches([1, 0, 1]))