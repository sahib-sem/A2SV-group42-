"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        mapping = {}
        for employee in employees:
            mapping[employee.id] = employee
        
        def dfs(employee):
            if employee.subordinates == []:
                return employee.importance
            
            count = employee.importance
            
            for subordinate in employee.subordinates:
                subordinate = mapping[subordinate]
                res = dfs(subordinate)
                count += res
            return count 
                    
            
        for employee in employees:
            if employee.id == id:
                return dfs(employee)
                
        
        
        