
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: list[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees: list['Employee'], id: int) -> int:
        dic = dict()
        for emp in employees:
            dic[emp.id] = emp
        
        def dfs(root):
            nonlocal ans
            if not root:
                return
            ans += root.importance
            for id in root.subordinates:
                dfs(dic[id])
        
        ans = 0
        dfs(dic[id])
        return ans
            