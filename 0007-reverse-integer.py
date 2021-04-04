# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        num = 0
        neg = 1
        if x < 0:
            neg = -1
            x = abs(x)

        while(x!=0):
            num = num*10 + (x%10)
            x = x//10
        
        return int(num*neg) * int(-(2**31) <= num and num <= 2**31 - 1)