'''
Suppose you have a row of seats, some of which are occupied ('x') and some are empty ('.'). 
Your task is to arrange all the occupied seats together in one contiguous group.
Find the minimum number of moves required
'''

def minMoves(seats):
    crosses = [i for i,c in enumerate(seats) if c == 'x']
    # print(crosses)
    middle = len(crosses)//2
    left = crosses[0:middle]
    left.reverse()
    # print(left)
    cost = 0
    lb = crosses[middle]-1
    for i in left:
        # print(i," ",lb)
        if lb == i:
            lb-=1
        else:
            cost+=abs(lb-i)
            lb-=1
    right = crosses[middle+1:]
    # print(right)
    rb = crosses[middle]+1
    for i in right:
        # print(i," ",rb)
        if i == rb:
            rb+=1
        else:
            cost+=abs(rb-i)
            rb+=1
            
    return cost
    
    
print(minMoves('xx..xx....xxx'))
print(minMoves('.x..x..xx.'))
print(minMoves('..x..x.'))