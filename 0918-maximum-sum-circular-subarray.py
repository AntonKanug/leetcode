# https://leetcode.com/problems/maximum-sum-circular-subarray/
# medium


# 1. Max subarray needs NO wrap around -> kadane
# 2. Max subarray NEEDS wrap around -> sum - min sub array

class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        
        noWrapSum = self.kadane(A)
        
        cirSum = sum(A)
        A = [-i for i in A]
        
        cirSum += self.kadane(A)
        
        if cirSum:
            return max(cirSum, noWrapSum)
        return noWrapSum
    

    def kadane(self, A):
        sum1, output = A[0], A[0]

        for i in A[1:]:  
            sum1 = max(i, sum1+i)
            output = max(sum1, output)
                
        return output
            
        
        
    