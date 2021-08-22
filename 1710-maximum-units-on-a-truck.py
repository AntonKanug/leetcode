# https://leetcode.com/problems/maximum-units-on-a-truck/

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1])
        
        output = 0
        
        for boxes, units in boxTypes[::-1]:
            if boxes <= truckSize:
                truckSize -= boxes
                output += units*boxes
            else:
                output += units*(truckSize)
                break
    
        return output
