# https://leetcode.com/problems/employee-importance/
 
"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    dicto = {}
    
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        # Create dict
        for employee in employees:
            self.dicto[employee.id] = employee
        return self.importance(self.dicto[id]) 

    def importance(self, employee):
        if not employee.subordinates:
            return employee.importance
        sum = 0
        for subs in employee.subordinates:
            sum += self.importance(self.dicto[subs])
            
        return sum + employee.importance