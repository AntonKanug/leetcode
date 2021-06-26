# https://leetcode.com/problems/kth-largest-element-in-an-array/submissions/
# O(n) - Time, n + n/2 + n/4 ... = n(1 + 1/2 + 1/4) = n(2) = O(n)
# O(n) - Space, partition arrays

# Idea:
# Partition arr by random element
# Check which partition the k element is in
# Continute the process until kth element = partition

import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def helper(nums: List[int], k: int):

            # partition
            idx = random.randint(0, len(nums)-1)
            partitioner = nums[idx]

            smaller = []
            bigger = []

            for j, i in enumerate(nums):
                if j == idx: continue
                
                if i < partitioner:
                    smaller.append(i)
                else:
                    bigger.append(i)
            
            # Partition = kth element
            if k-1 == len(smaller): return partitioner
            
            # Kth element is in smaller partition
            elif k <= len(smaller): return helper(smaller, k)
            
            # Kth element is in bigger partition
            else: return helper(bigger, k - len(smaller) - 1)
        
        # Helper used to find kth smallest element 
        return helper(nums, len(nums)-k+1)
            
            
