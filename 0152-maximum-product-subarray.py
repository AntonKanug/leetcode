# https://leetcode.com/problems/maximum-product-subarray/submissions/

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxv = float('-inf')
        maxcurr, mincurr = 1, 1
        
        for i in nums:
            maxcurr, mincurr = max(maxcurr * i, mincurr * i, i), min(maxcurr * i, mincurr * i, i)
            maxv = max(maxcurr, maxv)

        return maxv
    