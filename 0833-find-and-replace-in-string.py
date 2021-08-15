# https://leetcode.com/problems/find-and-replace-in-string/

class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        items = [[indices[i], sources[i], targets[i]] for i in range(len(indices))]        
        items.sort(key=lambda x: x[0])
        
        for i, src, tgt in items[::-1]:
            if src == s[i:i+len(src)]:
                s = s[:i] + tgt + s[i+len(src): ]
        
        return s