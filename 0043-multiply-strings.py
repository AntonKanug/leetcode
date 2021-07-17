# https://leetcode.com/problems/multiply-strings/submissions/
# Time - O(n^2)
# Space - O(1)

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = 0
        
        for mainFactor, i in enumerate(num1[::-1]):
            for factor, j in enumerate(num2[::-1]):
                res += (ord(j) - ord('0')) * (ord(i) - ord('0')) * (10 ** (factor + mainFactor))
                
        return str(res)
    
    
