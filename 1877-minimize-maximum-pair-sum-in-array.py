# https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        minmax = float('-inf')
        
        for i in range(len(nums)//2):
            minmax = max(minmax, nums[i] + nums[-1-i])

        return minmax
    