# https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/submissions/
# Time - O(n)
# Space - O(n)

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        
        hmap = {}
        for i in arr:
            if i in hmap: hmap[i] +=1
            else: hmap[i] = 1
                
        # {num of repeats: how many nums are repeated}
        items = {}
        for i in hmap:
            if hmap[i] in items: items[hmap[i]] += 1
            else: items[hmap[i]] = 1
        
        output = len(hmap)

        for i in range(len(arr)+1):
            if i not in items: continue
            for _ in range(items[i]):
                if i <= k:
                    k -= i
                    output -= 1
                
        return output