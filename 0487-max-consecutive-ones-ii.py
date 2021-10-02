# https://leetcode.com/problems/max-consecutive-ones-ii/submissions/

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        sums = [0]
        maxs = 0
        
        for i in nums:
            if i: sums[-1]+=1
            else:
                maxs = max(maxs, sum(sums)+1)
                if len(sums) < 2: sums.append(0)
                else: sums[0], sums[1] = sums[1], 0

        if len(sums) == 1:
            return sums[-1]
        
        return max(maxs, sum(sums)+1)
    
