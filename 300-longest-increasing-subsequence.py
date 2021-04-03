# https://leetcode.com/problems/longest-increasing-subsequence/
# dp medium

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        temp = [1]*len(nums)
        
        for i in range(1,len(nums)):  
            # i, j pointers to 0 and end of sub array
            
            for j in range(i):
                if nums[j] < nums[i] and temp[j]+1 > temp[i]:
                    temp[i] = temp[j]+1
                
        return max(temp)