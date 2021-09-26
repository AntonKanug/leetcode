# https://leetcode.com/problems/exclusive-time-of-functions/

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        res = [0]*n
        
        for log in logs:
            i, call, time = log.split(':')
            i, time = int(i), int(time)
            
            if call == 'end' and stack[-1][0] == (i,'start'):
                diff = time - stack[-1][1] + 1
                res[i] += diff - stack[-1][2]
                temp = stack.pop()
                
                if stack: stack[-1][2] += diff
                    
            else: stack.append([(i,call), time, 0])

        return res
    