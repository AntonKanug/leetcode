# https://leetcode.com/problems/make-the-string-great/

class Solution:
    def makeGood(self, s: str) -> str:
        stack = []

        for i in s:
            if (stack and abs(ord(i)-ord(stack[-1])) == 32):
                stack.pop()
            else:
                stack.append(i)
                
        output = ''  
        for i in stack:
            output+=i
            
        return output