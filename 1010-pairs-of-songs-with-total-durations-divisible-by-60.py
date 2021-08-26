# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/submissions/

# (time[i] + time[j]) % 60 == 0
# 60 (time[i]) % 60 =  time[j] % 60

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        
        nums = {}
        output = 0
        
        for i in time:
            numCheck =  60 - (i % 60)
            if numCheck == 60: numCheck = 0
   
            if numCheck in nums:
                output += nums[numCheck] 
                    
            if i%60 in nums: nums[i%60]+=1
            else: nums[i%60] = 1

        return output