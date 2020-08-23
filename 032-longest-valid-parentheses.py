# https://leetcode.com/problems/longest-valid-parentheses/

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        stack = [-1]
        max = 0
        
        for i in range(len(s)):
            if ord(s[i])-ord(s[stack[-1]]) == 1:
                stack.pop()
                if not stack:
                    stack.append(i)
                if (i - stack[-1]>max):
                    max = i - stack[-1]
            else:
                stack.append(i)
        return max