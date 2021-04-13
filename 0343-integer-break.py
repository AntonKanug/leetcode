# https://leetcode.com/problems/integer-break/submissions/
# medium

class Solution:
    def integerBreak(self, n: int) -> int:
        if n<=3:
            return n-1
        
        num3s = n//3
        rem = n%3
        num2s = rem//2
        
        if rem == 1:    
            num3s-=1
            num2s=2

        return (3**(num3s))* (2**(num2s))
            
