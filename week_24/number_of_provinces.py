class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        adj_list = dict()
        for i in range(len(isConnected)):
            adj_list[i+1] = []
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if i != j and isConnected[i][j] == 1:
                    adj_list[i+1].append(j+1)
        
        def dfs(node):
            visited.add(node)
            for neighbour in adj_list[node]:
                if neighbour in visited:
                    continue
                dfs(neighbour)

        visited = set()
        count = 0
        for key in adj_list.keys():
            if key not in visited:
                count += 1
                dfs(key)
        return count