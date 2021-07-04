# https://leetcode.com/problems/buildings-with-an-ocean-view/submissions/
# O(n) - Time
# O(1) - Space, not including output

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        
        output = []
        tallest = 0
        buildings = len(heights) - 1
        
        for i, j in enumerate(heights[::-1]):
            if j > tallest:
                output.append(buildings - i)
                tallest = j
                
        return output[::-1]
    
