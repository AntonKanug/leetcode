# https://leetcode.com/problems/remove-element/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        right = 0
        
        while(left+right!=len(nums)):
            if nums[left] == val:
                nums[-1-right], nums[left] = val, nums[-1-right]
                if(nums[left]==val):
                    left-=1
                right+=1
            left+=1
        
        # Faster than slicing ?
        for i in range(right):
            nums.pop()
        
        return len(nums)