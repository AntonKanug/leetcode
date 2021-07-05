# https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/submissions/
# O(nlgn) - Time,s sorting
# O(1) - Space

# Find max diff in v and h => vDiff*hDiff

class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        
        horizontalCuts.sort()
        verticalCuts.sort()
        
        horizontalCuts.append(h)
        verticalCuts.append(w)
        
        maxH = horizontalCuts[0]
        maxV = verticalCuts[0]
        
        for i in range(len(horizontalCuts)-1):
            maxH = max(maxH, horizontalCuts[i+1] - horizontalCuts[i])   
        
        for i in range(len(verticalCuts)-1):
            maxV = max(maxV, verticalCuts[i+1] - verticalCuts[i])   
              
        return maxV * maxH % (10**9 + 7)
        
        
