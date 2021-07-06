# https://leetcode.com/problems/number-of-good-ways-to-split-a-string/submissions/
# O(n) - Time
# O(1) - Space, size 26 alphabet

# Idea:
# Count all the chars and keep and array of size 26 (call it right)
# Go through string, each iteration --1 from right array and the letter to set
# If length of left letter set == right letter count => good++
# Return good count

class Solution:
    def numSplits(self, s: str) -> int:
        good = 0
        
        right = [0] * 26
        rightLetters = 0
        leftLetters = set()
        
        for i in s:
            # New letter
            if not right[ord(i) - ord('a')]: rightLetters += 1
            right[ord(i) - ord('a')] += 1
            
        for i in s:
            leftLetters.add(i)
            
            right[ord(i) - ord('a')] -= 1
            if not right[ord(i) - ord('a')]: rightLetters -= 1

            if len(leftLetters) == rightLetters: good+=1
        
        return good
        
