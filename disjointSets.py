'''
Given a list of intervals, the problem asks you to 
find the length of the maximum set of mutually disjoint 
intervals. Disjoint intervals are intervals that don't 
overlap with each other.
'''

def maxDisjoint(A):
    # End early
    A.sort(key = lambda x : x[1])
    
    prev_s, prev_e = A[0]
    count = 1
    
    for s,e in A:
        if s<= prev_e:
            pass
        else:
            prev_s,prev_e = s,e
            count+=1
    return count

# Test cases
print(maxDisjoint([(1, 2), (2, 3), (3, 4), (5, 6)]))  
print(maxDisjoint([(1, 2), (2, 3), (3, 4), (4, 5)]))  
print(maxDisjoint([(1, 4), (2, 3), (3, 6), (7, 8)]))  
print(maxDisjoint([(1, 4), (2, 5), (6, 7), (8, 9)]))  
print(maxDisjoint([(1, 3), (2, 4), (5, 6), (7, 8)]))  
