# https://leetcode.com/problems/minimum-operations-to-make-array-equal/
# medium

class Solution:
    def minOperations(self, n: int) -> int:
        toAdd = n-1
        sum = 0
        while(toAdd > 0):
            sum += toAdd
            toAdd -= 2
            
        #  (n*n)/4
        return sum
