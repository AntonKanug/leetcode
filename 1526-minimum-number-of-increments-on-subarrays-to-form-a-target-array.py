# https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/submissions/

class Solution:
#     def minNumberOperations(self, target: List[int]) -> int:
        
#         output = 0
#         t = sorted([(j,i) for i,j in enumerate(target)], key=lambda x: x[0])
#         lastVal = 0
        
#         for val, idx in t:
#             output += target[idx]
#             x = target[idx]
            
#             # go left
#             l = idx
#             while(l >= 0 and target[l]):
#                 target[l] =  target[l] - x
#                 l -= 1
                
#             # go right
#             r = idx+1
#             while(r < len(target) and target[r]):
#                 target[r] =  target[r] - x
#                 r += 1

 def minNumberOperations(self, target: List[int]) -> int:
        
        last = 0
        output = 0
        
        for i in target:
            if i-last > 0: output += i-last
            last = i

        return output