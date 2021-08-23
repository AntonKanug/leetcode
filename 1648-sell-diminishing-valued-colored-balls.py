# https://leetcode.com/problems/sell-diminishing-valued-colored-balls/submissions/

from decimal import Decimal

class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        inventory.append(0)
        inventory.sort()
        inventory = inventory[::-1]
        
        def sumAB(a, b):
            b+=1
            return (Decimal(a-b+1)*Decimal(a+b)/2)
        
        output = 0
        i = 0

        while i < len(inventory):
            
            curVal = inventory[i]
            nextVal = 0
            
            while i < len(inventory) and curVal == inventory[i]:
                i+=1
            
            if i < len(inventory): 
                nextVal = inventory[i] 
            
            if i*(curVal - nextVal) > orders:
                output += i*sumAB(curVal, curVal - orders//i)
                output += orders%i * (curVal - orders//i )
                break
            else:
                output += i*sumAB(curVal, nextVal)
                orders -= i*(curVal-nextVal)
            
            if orders < 0: break

        return output%((10**9) +7)