# https://leetcode.com/problems/length-of-last-word/


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        size = 0

        for i in range(len(s)):
            if s[len(s)-i-1]==' ' and not size: continue
            if s[len(s)-i-1]!=' ':  size+=1
            else: return size
            
        return size