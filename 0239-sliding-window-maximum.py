# https://leetcode.com/problems/sliding-window-maximum/

from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = [None]*(len(nums))
        dq = deque()
                
        for i in range(len(nums)):
            
            # Removing out of left 
            while dq and dq[0] < i-k+1:
                dq.popleft()

            # Removing out of right 
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)
            
            output[i] = nums[dq[0]]

        
        return output[k-1:]