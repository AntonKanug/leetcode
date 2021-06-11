# https://leetcode.com/problems/consecutive-numbers-sum/

# x + (x+1) + (x+2) ... = n

# x = n
# 2x + 1 = n
# 3x + 3 = n
# 4x + 6 = n

# ax + b = n
# (n - b)/ = x (has to be divisible)
# if (n-b)//x == 0; end loop

class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        if n <= 2: return 1
        
        # (N-b)/a
        count = 0
        
        plus = 0
        div = 0
        
        for i in range(n):
            plus+=i
            div+=1
            
            if not (n - plus)//div: return count
            if not (n - plus)%div: count+=1
