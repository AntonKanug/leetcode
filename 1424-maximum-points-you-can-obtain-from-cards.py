# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/submissions/
# medium 

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        # Add up all left [0-k]
        maxSum = 0
        for i in range(k):
            maxSum+=cardPoints[i]
        
        # Remove 1 left add 1 right
        tempSum = maxSum
        for i in range(k):
            tempSum += cardPoints[-(i+1)] - cardPoints[k-i-1] 
            
            if tempSum > maxSum:
                maxSum = tempSum
                
        return maxSum
            
            
        