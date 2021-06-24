# https://leetcode.com/problems/median-of-two-sorted-arrays/submissions/
# O(lg min(m,n)) - Time
# O(1) - space
# Hard

# Idea:
# Do binary search in smallest array
# Each time to calculate partitiions in x and y arr
# partitionX + partitionY = (x+y+1)//2
# Calculate max and min of each partition for left and right
# Cross reference them to see if this partition is correct => found
# Else max left of x > min right of Y => bin search in left of x
# Else bin search in right of x


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        x, y =  len(nums1), len(nums2)
        l, r = 0, x
        
        while (l<=r):
            partX = (l+r)//2
            partY = (x+y+1)//2 - partX
            
            maxLX = float('-inf') if partX == 0 else nums1[partX-1]
            minRX = float('inf') if partX == x else nums1[partX]
            
            maxLY = float('-inf') if partY == 0 else nums2[partY-1]
            minRY = float('inf') if partY == y else nums2[partY]
            
            
            if (maxLX <= minRY and maxLY <= minRX):
                if (x+y) % 2 == 0:
                    return (max(maxLX, maxLY) + min(minRX, minRY))/2
                else: 
                    return max(maxLX, maxLY)
                
            elif (maxLX > minRY): r = partX -1
            else: l = partX + 1

        return -1
