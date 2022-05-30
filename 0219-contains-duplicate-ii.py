# https://leetcode.com/problems/contains-duplicate-ii/
# O(n) - Time
# O(n) Space

# Heuristic:
# always i > j (i enumerates)
# i - j < k
# i < k + j

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        nums_dict = {}

        for (i, num) in enumerate(nums):
            if num in nums_dict and i <= k + nums_dict[num]:
                return True
            nums_dict[num] = i

        return False
    