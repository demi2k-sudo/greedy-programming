'''
You're planning a road trip and want to know if it's possible to 
travel around a circular route of gas stations. Each gas station 
provides a certain amount of gas and requires a certain amount of 
gas to travel to the next gas station. Your task is to determine 
the starting gas station index from where you can complete the 
circular route without running out of gas.
'''

def travelAround(gasStations, cost):
    n = len(gasStations)
    
    curr = start = 0
    
    for i, (g,c) in enumerate(zip(gasStations*2,cost*2)):
        
        if i == start + n:
            return start
        
        curr = curr + g - c
        
        if curr<0:
            start = i+1
            curr = 0
    return -1
            
print(travelAround([3,5,2,1,7],[4,2,1,9,1]))