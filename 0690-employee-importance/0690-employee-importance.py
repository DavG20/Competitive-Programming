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
        
        
        employe_impo = {e.id : e for e in employees }
        
        
        return self.dfs(employe_impo ,id )
    
    
    
    def dfs(self, employe_map , emp_id):
        curr_empl = employe_map[emp_id] 
        return curr_empl.importance  + sum(self.dfs(employe_map, e ) for e in curr_empl.subordinates)
        
        