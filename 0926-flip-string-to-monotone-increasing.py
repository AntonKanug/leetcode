# https://leetcode.com/problems/flip-string-to-monotone-increasing/
# medium

class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:

        ones = 0
        flip = 0
        
        
        for i in S:
            if i == '0':
                if not ones:
                    continue
                else:
                    flip+=1
            else:
                ones+=1
                
            if flip > ones:
                flip = ones
        
        return flip
        