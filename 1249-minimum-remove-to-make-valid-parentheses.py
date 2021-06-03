# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/submissions/
# O(n) - time
# O(n) - space (stack)
# medium

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        
        for i,l in enumerate(s):
            if stack and l == ')' and stack[-1][0] == '(':
                stack.pop()
            elif l in ['(',')']:
                stack.append((l,i))
                
        size = len(stack)
        
        # Reverse stack and remove elements
        for i in range(size):
            s = s[:stack[size-i-1][1]] + s[stack[size-i-1][1]+1:]
                
        return s