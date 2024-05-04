'''
Given a list of meetings represented by start and end times, 
the problem is to find the minimum number of meeting rooms required 
such that no two meetings overlap in the same room.
'''

def maxRooms(A):
    data = []
    for i in A:
        data.append((i[0],+1))
        data.append((i[1],-1))
    data.sort(key=lambda x:x[0])
    max = 0
    curr = 0
    for _,room in data:
        curr+=room
        if curr>max:
            max = curr
    return max
    
print(maxRooms([[5,10],[15,20],[0,30]]))