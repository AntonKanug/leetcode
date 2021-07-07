# https://leetcode.com/problems/minimum-time-difference/submissions/
# O(nlgn) - Time, sort
# O(n) - Space

# Could be done in O(n) time by using O(2400) size array
# Create arr size of (24*60) of bool (all false)
# Iterate again and arr[i.value] = True
# Find min diff of true vals and max
# Trade off is size 2400 array 

# Idea:
# hours * 60 + mins
# Sort 
# Find max and min
# Return min(minChange, 24*60 - maxChange)

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        times = []
        zeroExists = False
        
        for i in timePoints:
            splitRes = i.split(':')
            val = int(splitRes[0]) * 60 + int(splitRes[1])
            times.append(val)
        
        times.sort()
        minChange = float('inf')
        maxChange = times[-1] - times[0]

        for i in range(len(times)-1):
            minChange = min(minChange, times[i+1] - times[i])
        
        return min(minChange, 1440 - maxChange)          
    
