# https://leetcode.com/problems/max-consecutive-ones-iii/

from collections import *

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
    
        dq = deque()
        zeros = 0
        maxs = 0

        for i in nums:    
            dq.append(i)
            
            if not i: zeros+=1

            while zeros>k:
                if not dq.popleft(): zeros-=1

            maxs = max(maxs, len(dq))

        return maxs

