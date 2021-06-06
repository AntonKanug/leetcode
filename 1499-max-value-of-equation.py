# Using deque (slideing window)
# Condition is xj-xi < k
# O(n) - time
# O(n) - space
# hard
  
class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        q = collections.deque()
        maxval = float('-inf')
        
        for x,y in points:
            # Remove all the invalid coods by conditon xj-xi <= k
            while q and q[0][0] < x-k: 
                q.popleft()
                
            # Calc maxval
            if q: maxval = max(maxval, q[0][1] + y + x)
                
            # Remove all smaller values by y-x in q
            while q and q[-1][1] <= y-x:
                q.pop()
            q.append([x,y-x])

        return maxval
