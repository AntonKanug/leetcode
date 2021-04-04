# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max1=0
        i = 0
        j = len(height)-1
       
        while(i!=j):
            
            if height[i] < height[j]:
                max2 = height[i]*(j-i)
            else:
                max2 = height[j]*(j-i)
    
            if(max2>max1):
                max1=max2

            if (height[i]>height[j]):
                j-=1
            else:
                i+=1

        return max1