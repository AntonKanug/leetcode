# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        for i in s:
            if stack and (ord(i)-stack[-1] in [1,2]):
                stack.pop()
            else:
                stack.append(ord(i))
        
        return not bool(stack)