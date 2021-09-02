# https://leetcode.com/problems/first-missing-positive/

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums[i]-=1
        
        for i, num in enumerate(nums):
            while num >= 0 and num < len(nums) and num != i:
                nums[i], nums[num] = nums[num], nums[i]
                if nums[i] == nums[num]: break
                num = nums[i]
        
        for i, num in enumerate(nums):
            if i != num: return i+1
        
        return len(nums)+1
        