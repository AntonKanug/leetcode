# https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/
# O(n) - Time
# O(n) - space (only need queue not dq)

# Pop from q until there is no str[i] 
# Append str[i]
# Max (count, length of q)

from collections import deque
import heapq
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        letters = {}
        for i in s: letters[i] = 0

        dq = deque()
        
        for i in s:
            while dq and letters[i]:
                x = dq.popleft()
                letters[x] -= 1
            dq.append(i)
            letters[i]+=1
            
            count = max(count, len(dq))
        
        return count
      
