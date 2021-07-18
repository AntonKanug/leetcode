# https://leetcode.com/problems/reverse-bits/submissions/
# Time - O(1)
# Space - O(1)

# Get last bit and add it to ans
# Shift bits left by 1
# Shift n right by 1
# Do it for all 32 bits
# Return ans but shift right by 1

class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        
        for _ in range(32):
            ans += (n & 1)
            ans <<= 1
            n >>= 1
        
        return ans >> 1
        
