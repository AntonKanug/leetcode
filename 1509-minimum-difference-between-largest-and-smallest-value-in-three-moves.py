# https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/submissions/
# medium 
# O(nlgn) - sorting
# O(1) - space

# Idea
# Remove 3 max
# Remove 3 min
# Remove 1 min, 2 max
# Remove 2 min, 1 max
# Check all -> pick lowest


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if (len(nums)<=4): return 0
        
        nums.sort()

        mindist = float('inf')
        min4 = nums[:4]
        max4 = nums[-4:]
        
        for i in range(4):
            if (max4[i] - min4[i] < mindist): mindist = max4[i] - min4[i]
                
        return mindist
