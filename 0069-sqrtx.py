# https://leetcode.com/problems/sqrtx/submissions/
# O(lgx) - Time
# O(1) - Space

# Idea 
# Bin search with mid * mid and x as the comparison
# If mid*mid < x => left = mid + 1
# Else => right = mid - 1

class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1: return x
        l,r = 1,x
        
        while l <= r:
            mid = (r+l)//2
            val = mid * mid
            
            if val == x : return mid
            elif val < x:  l = mid + 1
            else: r = mid - 1
                
        
        return l - 1
    
