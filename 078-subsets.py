# https://leetcode.com/problems/subsets/submissions/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for i in nums:
            temp = []
            for j in result:
                temp.append(j + [i])
            result += temp
        return result
        