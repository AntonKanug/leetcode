# https://leetcode.com/problems/letter-combinations-of-a-phone-number/submissions/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        
        nums = { '2': ['a','b','c'], \
                '3': ['d','e','f'], \
                '4': ['g','h','i'], \
                '5': ['j','k','l'], \
                '6': ['m','n','o'], \
                '7': ['p','q','r','s'], \
                '8': ['t','u','v'], \
                '9': ['w','x','y','z'] }
        
        output = nums[digits[0]]
        
        for num in str(digits)[1:]:
            temp = []
            for i in output:
                for j in nums[num]:
                    temp.append(i+j)
                    
            output = temp
                    
        return output
    