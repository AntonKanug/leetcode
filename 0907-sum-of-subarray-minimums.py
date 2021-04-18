# https://leetcode.com/problems/sum-of-subarray-minimums/
# += A[i](num smaller on left + 1) * (nums_smaller on right + 1) 

# A=[3,1,2,5,4]
# 3
# 1 + 1
# 1 + 1 + 2
# 1 + 1 + 2 + 5
# 1 + 1 + 2 + 4 + 4
# result = [3,2,4,9,12]
# N^2 approach

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        minArr = [float(inf)]*len(arr)
        sum = 0
        
        for i in range(len(arr)):
            for j in range(i+1):
                
                if arr[i]<minArr[j]:
                    minArr[j] = arr[i]
                sum += minArr[j]
                
        return sum%(10**9 + 7)
                