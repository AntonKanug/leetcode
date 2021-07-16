# https://leetcode.com/problems/permutations/submissions/
# Time - O(n!) 
# Space - O(n!) Return outpupt, else size n recrusion depth


# Idea:
# Recrusively call permute with an array that doesnt include the cur elemt
# Combine cur num and result and append
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1: return [nums]
        
        res = []
        for i in range(len(nums)):
            for j in self.permute(nums[:i] + nums[i+1:]):
                    res.append([nums[i]] + j)
                  
        return res
    
