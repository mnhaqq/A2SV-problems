class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u, v, t in roads:
            graph[u].append((v, t))
            graph[v].append((u, t))

        heap = [(0, 0)]
        nodes = [float('inf')] * n
        visited = set()

        while heap:
            time, node = heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            nodes[node] = time

            for v, t in graph[node]:
                if v not in visited:
                    heappush(heap, (t + time, v))
        
        mini = nodes[-1]
        visited = set()
        memo = {}

        def dp(i, cost):
            if i == 0:
                return 1
            
            ans = 0
            if i not in memo:
                for v, t in graph[i]:
                    if t + cost + nodes[v] == mini:
                        ans += dp(v, t + cost)
                memo[i] = ans
            return memo[i]
        
        ans = dp(n-1, 0) % ((10 ** 9) + 7)
        return ans
