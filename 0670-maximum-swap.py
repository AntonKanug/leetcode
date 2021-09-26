# https://leetcode.com/problems/maximum-swap/submissions/

class Solution:
    def maximumSwap(self, num: int) -> int:
        res = list(str(num))

        idxs = {}
        for i, val in enumerate(str(num)):
            idxs[int(val)] = i
        
        for i, val in enumerate(str(num)):
            for j in range(9,int(val),-1):
                if j in idxs and idxs[j] > i:
                    res[i], res[idxs[j]] = res[idxs[j]], res[i]
                    return int(''.join(res))

        return num
    
