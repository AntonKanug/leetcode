# https://leetcode.com/problems/product-of-array-except-self/submissions/
# O(n) - Time
# O(n) - Space

# Idea:
# Calculate all the left products (i) => nums[i-1] * nums[i-2] ... nums[0]
# Calculate all the right products (i) => nums[i+1] * nums[i+2] ... nums[len(nums)-1]
# Caluclate total products (i) => left[i] * right[i]

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # Calculate left of products
        left = [1]
        for i in nums[:-1]:
            left.append(left[-1] * i)

            
        # Calulcate righ products
        right = [1]
        for i in nums[::-1][:-1]:
            right.append(right[-1] * i)
        right = right[::-1]
        
        
        # Calculate total product 
        return [ left[i]*right[i] for i in range(len(left)) ]
    
            
