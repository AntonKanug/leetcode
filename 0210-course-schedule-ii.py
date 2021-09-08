# https://leetcode.com/problems/course-schedule-ii/

from collections import *
    
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        postreq = defaultdict(set)
        prereqs = defaultdict(set)
        
        for course, prereq in prerequisites:
            prereqs[course].add(prereq)
            postreq[prereq].add(course)
            
        bfs = [i for i in range(numCourses) if not prereqs[i]]
        
        for i in bfs:
            # for all the courses that this course is a prereq for
            for j in postreq[i]:
                # Remove the course from its prereq
                prereqs[j].remove(i)
                # If it has no more prereqs add it to bfs
                if not prereqs[j]: 
                    bfs += [j]
                    
        return bfs if len(bfs)==numCourses else []
        