class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        values = set()
        maxlen = 0
        
        for i in nums:
            values.add(i)
            
        for i in nums:
            tempLen = 1
            
            if (i in values): values.remove(i)
            else: continue
            
            # Try reducing values
            reducing = i-1
            while(reducing in values):
                tempLen+=1
                values.remove(reducing)
                reducing-=1
                
            # Try increasing values
            increasing = i+1
            while(increasing in values):
                tempLen+=1
                values.remove(increasing)
                increasing+=1
                
            if maxlen < tempLen: maxlen = tempLen
                
        return maxlen