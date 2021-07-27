# https://leetcode.com/problems/combination-sum/submissions/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        
        def helper(arr, target, start):
            if target == 0: 
                res.append(arr)
                return
            
            for j, i in enumerate(candidates[start:]):
                if i <= target:
                    helper(arr + [i], target - i, j+start)
                else: break
            
            return res
        
        x = helper([], target, 0)
        return x
        