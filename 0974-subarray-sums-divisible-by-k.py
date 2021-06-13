# https://leetcode.com/problems/subarray-sums-divisible-by-k/submissions/

# sum[i]-sum[j] = k*x (x = some value)
# (sum[i]-sum[j])%k = k*x % k
# (sum[i]-sum[j])%k = 0
# sum[i] % k = sum[j] %k
# => add all sums that had remainder as current sum while iterating

# O(n) - time
# O(k) - space

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        
        remainders = {}
        remainders[0] = 1
        
        res = 0
        count = 0
        
        for i in nums:
            count += i
             
            rem = (count%k + k) % k
            
            if rem in remainders:
                res += remainders[rem]
                remainders[rem] +=1 
            else:
                remainders[rem] = 1

                
        return res
             
