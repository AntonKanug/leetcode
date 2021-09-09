# https://leetcode.com/problems/decode-ways/

class Solution:
    def numDecodings(self, s: str) -> int:
        if (not s or s[0] == '0'): return 0
        
        r1,r2 = 1,1
        
        for i,val in enumerate(s[1:]):
            i +=1 
            
            if val == '0': r1 = 0
                
            r = r1
            if (s[i-1] == '1' or (int(val)<=6 and s[i-1] =='2')):
                r1 += r2
    
            r2 = r
                
        return r1    
    