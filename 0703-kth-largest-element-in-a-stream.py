# https://leetcode.com/problems/kth-largest-element-in-a-stream/submissions/
# O(n) - Time, initial heapify
# O(lg k) - Time, add 
# O(k) - Space, heap

# Idea:
# Keep max heap of size k
# When adding check if size is bigger than k => pop
# Return top of max heap

import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        
        heapq.heapify(self.nums)
        
        for i in range(len(nums)-k):
            heapq.heappop(self.nums)
        
    def add(self, val: int) -> int:
        heapq.heappush(self.nums,val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)

        return list(self.nums)[0]
        
        
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
