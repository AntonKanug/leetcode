# https://leetcode.com/problems/group-anagrams/
# O(n) - Time, sorting is constant (100 max len)
# O(n) - space, hashmap

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}
        
        for i in strs:
            word = i
            si = ''.join(sorted(i))
            
            if si in words: words[si].append(word)
            else: words[si] = [word]
                
        return words.values()
    