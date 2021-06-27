# https://leetcode.com/problems/meeting-rooms-ii/submissions/
# O(nlgn) - Time, sorting
# O(n) - Space, sorted array

# Idea:
# Have array of room adds and removes (+-1)
# Sort it by time
# Add the values -> return the max at one time 

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        # Times where rooms are added and removed
        sortedInt = []
        for i, j in intervals:
            sortedInt.append([i, 1])
            sortedInt.append([j, -1])
        
        # Sort times
        sortedInt.sort(key=lambda x: x[0])

        tc, maxc = 0, 0 
        i = 0
        length = len(sortedInt)

        # Add up all the additions and removals
        # Return the max
        while i<length:
            time = sortedInt[i][0]
            while i<length and time == sortedInt[i][0]:
                tc += sortedInt[i][1]
                i += 1

            maxc = max(maxc, tc)
        
        return maxc
    
