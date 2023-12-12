from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        def inbound(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid)

        moves = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        visited = set([(0,0)])

        count = 0
        queue = deque()
        queue.append((0,0))
        if grid[0][0] == 1:
            return -1

        while queue:
            len_level = len(queue)
            count += 1
            for _ in range(len_level):
                r, c = queue.popleft()
                if r == c == len(grid) - 1:
                    return count
                    
                for a, b in moves:
                    if not inbound(r+a, c+b):
                        continue
                    if grid[r+a][c+b] == 1:
                        continue
                    if (r+a, c+b) not in visited:
                        visited.add((r+a, c+b))
                        queue.append((r+a, c+b))
        
        return -1