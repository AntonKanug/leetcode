# https://leetcode.com/problems/k-closest-points-to-origin/submissions/
# O(nlgn) - Time, sorting
# O(n) - Space, sorted array
# Could also use maxheap

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        dist = sorted([ ((x**2 + y**2)**0.5, [x,y]) for x, y in points ], key=lambda x: x[0])
        
        output = []
        i = 0
        
        while i < k:
            output.append(dist[i][1])
            i+=1
            
        return output
        
