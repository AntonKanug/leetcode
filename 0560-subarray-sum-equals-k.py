# https://leetcode.com/problems/subarray-sum-equals-k/
# O(n) time
# O(n) space

# Idea
# Keep a sum of all nums 
# Keep hashmap with all vals as keys and sums as values
# At each iteration add sum-k to the result
# Note: Duplicate sums only exist due to 0 or negatives 

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        sums = {}
        sums[0] = 1
        
        count, res = 0, 0
        
        for i in nums:
            count += i
            
            if count-k in sums:
                res+=sums[count-k]
                
            if count in sums: sums[count] += 1
            else: sums[count] = 1

        return res
            
            
