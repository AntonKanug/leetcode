# https://leetcode.com/problems/car-fleet/submissions/

# Idea 
# Sort all cars by positions
# Calculate time it takes to reach end
# Every car thats behind the slowerst car (by TIME not speed) will become one fleet
# Update longest time
# Repeat

# O(nlgn) - time
# O(n) - sorted p + s array

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = 0
        
        cars = sorted(list(zip(position, speed)), key=lambda a:a[0])
        time = []
        
        for p, s in cars:
            time.append(float(target - p) / s)
        
        slowestTime = 0
        
        for t in time[::-1]:
             if t > slowestTime:
                fleets += 1
                slowestTime = t
        
            
        return fleets
      
