# https://leetcode.com/problems/3sum/submissions/

# sort nums
# iterate i and have L pointer R pointer
# If nums[i] + nums[l] + nums [r] == 0 found -> append
# Skip duplicates when found
# Else move left and right pointers


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        size = len(nums)
        res = []
        
        for i in range(size):
            l = i+1
            r = size-1
            
            # If duplicate skip
            if i and nums[i] == nums[i-1]: continue
                
            while (l<r):
                if not (nums[i] + nums[r] + nums[l]):
                    res.append([nums[i], nums[l], nums[r]])
                    
                    # Move l forward and ignore the duplicates
                    while l<r and nums[l] == nums[l+1]:
                        l+=1
                    # Move r back and ignore duplicates
                    while l<r and nums[r] == nums[r-1]:
                        r-=1
                        
                    l+=1
                    r-=1
                        
                elif nums[i] + nums[r] + nums[l] < 0: l+=1
                else: r-=1
  
        return res
  
