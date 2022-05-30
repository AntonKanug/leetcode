# https://leetcode.com/problems/top-k-frequent-elements/

# O(n) - Time
# O(n) - Space, hashmap

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        num_occur = {}
        occur_nums = {}
        
        for i in nums:
            if i in num_occur: num_occur[i]+=1
            else: num_occur[i]=1
                
        for i in nums:
            occur = num_occur[i]
            
            if occur in occur_nums:
                occur_nums[occur].add(i)
            else:
                occur_nums[occur] = set([i])
        
        x = len(nums)
        y = k
        res = []
        
        while y > 0:
            if x in occur_nums:
                res += list(occur_nums[x])
                y -= len(list(occur_nums[x]))
            x-=1
        
        return res[:k]
    