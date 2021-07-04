# https://leetcode.com/problems/maximum-subarray/submissions/
# O(n) - Time
# O(1) - Space

# Idea:
# A max subseq's sum should be either the currentSum + valur or value it self
# Keep track of the max subseq

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        tempMax = float('-inf')
        maxWholeSeq = float('-inf')
        
        for i in nums:
            tempMax = max(tempMax+i, i)
            maxWholeSeq = max(tempMax, maxWholeSeq)
            
        return maxWholeSeq
    
    
