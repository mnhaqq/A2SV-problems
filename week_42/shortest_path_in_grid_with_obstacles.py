from collections import deque

class Solution:
    def shortestPath(self, grid: list[list[int]], k: int) -> int:
        def inbound(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])

        m, n = len(grid), len(grid[0])
        queue = deque([(0, 0, 0)])
        visited = set()

        moves = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        ans = 0

        while queue:
            level = len(queue)
            for _ in range(level):
                r, c, obs = queue.popleft()
                if r == m - 1 and c == n - 1:
                    return ans
                if (r, c, obs) in visited:
                    continue
                visited.add((r, c, obs))
                
                for a, b in moves:
                    if not inbound(r+a, c+b):
                        continue
                    if grid[r+a][c+b] == 1 and obs+1 <= k:
                        queue.append((r+a, c+b, obs+1))
                    elif grid[r+a][c+b] == 0:
                        queue.append((r+a, c+b, obs))
                    
            ans += 1
        return -1  