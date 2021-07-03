# https://leetcode.com/problems/dot-product-of-two-sparse-vectors/submissions/
# O(n) - Time, optimized for having more 0s than 1s
# O(n) - Space, optimized for having more 0s than 1s

class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = {}
        
        for i, val in enumerate(nums):
            if val: self.nums[i] = val
                
    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        output = 0

        for i in self.nums:
            if i in vec.nums:
                output += self.nums[i] * vec.nums[i]
            
        return output

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
