# https://leetcode.com/problems/trapping-rain-water/submissions/
# O(n) - Time
# O(1) - Space
# hard

# Idea:
# Keep maxL and maxR 
# Smaller out of the two will leak
# Each iterations calculate new max and minMax - height[i]

class Solution:
    def trap(self, height: List[int]) -> int:
        
        # If empty arr -> 0
        if not len(height): return 0
        
        # Set maxes
        leftMax = height[0]
        rightMax = height[-1]
        
        # Set l and r pointers
        l = 0
        r = len(height)-1
        
        count = 0
        
        # While loop
        while (l<=r):
            # If leftmax < rightmax => leftmax will leak
            if leftMax < rightMax:
                # See if curr height bigger
                leftMax = max(leftMax,height[l])
                # Add water count 
                count += leftMax - height[l] 
                l+=1 # Increment
            else:
                rightMax = max(rightMax,height[r])
                count += rightMax - height[r] 
                r-=1

        return count
      
