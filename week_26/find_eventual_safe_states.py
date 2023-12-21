from collections import defaultdict, deque

class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        dic = defaultdict(int)
        adj_list = dict()
        for i in range(len(graph)):
            adj_list[i] = []
        
        for key in adj_list.keys():
            for val in graph[key]:
                adj_list[val].append(key)
            dic[key] = len(graph[key])
        
        queue = deque([key for key in dic if dic[key] == 0])
        ans = []
        while queue:
            node = queue.popleft()

            for nei in adj_list[node]:
                dic[nei] -= 1
                if dic[nei] == 0:
                    queue.append(nei)
            ans.append(node)
        ans.sort()
        return ans