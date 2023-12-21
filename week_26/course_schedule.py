from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        adj_list = dict()
        for i in range(numCourses):
            adj_list[i] = []
        for a, b in prerequisites:
            adj_list[b].append(a)
        
        dic = defaultdict(int)
        for key, arr in adj_list.items():
            for val in arr:
                dic[val] += 1
        
        queue = deque([key for key in adj_list if key not in dic])
        
        ans = []
        while queue:
            node = queue.popleft()

            for nei in adj_list[node]:
                dic[nei] -= 1
                if dic[nei] == 0:
                    queue.append(nei)
                    del dic[nei]
        
            ans.append(node)
        return len(ans) == numCourses
