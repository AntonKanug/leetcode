# https://leetcode.com/problems/total-hamming-distance/submissions/
# medium
# O(n) = 32*n

class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        ones = [0]*32

        for i in nums:
            for (idx,j) in enumerate('{:032b}'.format(i)):
                if (j=="1"): ones[idx] +=1
        
        sum = 0
        numCount = len(nums)
        for i in ones:
            sum += (numCount-i)*i
            
        return sum    
            