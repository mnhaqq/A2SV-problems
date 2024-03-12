class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #djikstra
        graph = defaultdict(list)

        for a, b, c in times:
            graph[a].append((b, c))
        
        heap = [(0, k)]
        ans = defaultdict(lambda: float("inf"))

        count = n
        res = float("-inf")

        while heap:
            cost, node = heappop(heap)
            if ans[node] <= cost:
                continue
            
            ans[node] = cost
            res = max(res, ans[node])
            count -= 1 

            for a, b in graph[node]:
                if ans[a] > (b + cost):
                    heappush(heap, (b + cost, a))

        return res if count == 0 else -1

    #floyd-warshall
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [[float('inf')] * n for _ in range(n)]

        for a, b, c in times:
            dist[a-1][b-1] = c
        
        for i in range(n):
            dist[i][i] = 0

        for h in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][h] + dist[h][j])
        
        ans = max(dist[k-1])
        if ans == float('inf'):
            return -1
        return ans
