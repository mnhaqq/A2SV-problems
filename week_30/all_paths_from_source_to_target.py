class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        n = len(graph)

        all_paths = []
        curr_path = [0]
        def dfs(node):
            if node == n - 1:
                all_paths.append(curr_path[:])
                return
            
            for nei in graph[node]:
                curr_path.append(nei)
                dfs(nei)
                curr_path.pop()
        
        dfs(0)
        return all_paths