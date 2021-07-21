# https://leetcode.com/problems/jump-game/submissions/
# Time - O(n)
# Space - O(1)

# Idea:
# Keep the index that is max reachable
# Iterate through all indices
# If cur idx > max reachable index => false
# if cur idx + val of the nums[idx] >= array len => true
# Recalc max jump

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxJump = 0
        
        for idx, val in enumerate(nums):      
            if idx > maxJump: return False
            elif idx + val >= len(nums)-1: return True
            
            maxJump = max(idx+val, maxJump)

        return False
    