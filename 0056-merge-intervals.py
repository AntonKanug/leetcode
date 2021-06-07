# https://leetcode.com/problems/merge-intervals/submissions/
# O(nlgn) - time (sorting)
# O(n) - space (merged list)

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals = sorted(intervals,key=lambda x: x[0])
        
        mergeList = [intervals[0]]

        for i in range(1, len(intervals)):
            if mergeList[-1][1] >= intervals[i][0]:
                mergeList[-1][1] = max(mergeList[-1][1], intervals[i][1])
            else:
                mergeList.append(intervals[i])
                
        return mergeList
 
