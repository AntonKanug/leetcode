# https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/
# medium

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        lo = 0
        hi = len(nums)-1
        # Find min
        
        while(lo<hi):
            mid = (lo+hi)//2
            if nums[mid] > nums[hi]: lo = mid+1
            else: hi = mid
                
        # Run bin_search twice on left of min & right of min
        r1 = self.bin_search(nums[:lo], target)
        if r1 != -1: return r1
        
        r2 = self.bin_search(nums[lo:],target)
        
        if r2 == -1: return -1
        else: return r2 + lo
        
        
    def bin_search(self, nums: List[int], x):
        if not len(nums): return -1
        
        lo = 0
        hi = len(nums)-1
        
        while (lo<hi):
            mid = (lo+hi)//2
            if nums[mid] == x: return mid
            if nums[mid] < x: lo = mid+1
            else: hi = mid-1
                
        if nums[lo] == x: return lo
        return -1