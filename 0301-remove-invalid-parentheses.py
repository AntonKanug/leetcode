# https://leetcode.com/problems/remove-invalid-parentheses/submissions/

from collections import *

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        level = set([s])

        while level:
            newLevel = set([])
            for s in level:
                if self.valid(s): newLevel.add(s)

            if newLevel: return list(newLevel)

            for s in level:    
                for x in range(len(s)):
                    if s[x] in ['(', ')']:
                        newLevel.add(s[:x] + s[x+1:])

            level = newLevel

    def valid(self,s):
        stack = []
        for i in s:
            if i == ')' and stack and stack[-1] == '(':
                stack.pop()
            elif i in ['(',')']: stack.append(i)
                
        return not stack
        