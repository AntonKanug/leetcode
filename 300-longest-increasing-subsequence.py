# https://leetcode.com/problems/longest-increasing-subsequence/
# dp medium

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        temp = [1]*len(nums)
        
        for i in range(1,len(nums)):  
            x,y = 0,i
            
            while x != y:
                if nums[x] < nums[y] and temp[x]+1 > temp[y]:
                    temp[y] = temp[x]+1
                
                x+=1

        return max(temp)