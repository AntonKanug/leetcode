# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        
        for i in s:
            if stack and stack[-1] == '(' and i == ')': stack.pop()
            else: stack.append(i)
                
        return len(stack)
    