# https://leetcode.com/problems/maximum-number-of-visible-points/

from math import *

class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        
        angles = []
        samePos = 0
        
        for x,y in points:
            if x == location[0] and y == location[1]:
                samePos+=1
            else:
                angles.append(atan2(y - location[1], x - location[0])*180/pi)

        angles.sort()
        angles = angles + [i+360 for i in angles]

        res = 0
        l = 0
        for r, ang in enumerate(angles):
            while ang - angles[l] > angle:
                l+=1
            res = max(r-l+1, res)
        return res + samePos