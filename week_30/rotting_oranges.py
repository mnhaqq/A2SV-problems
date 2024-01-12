from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        def inbound(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])

        queue = deque()
        count_fresh = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    count_fresh += 1
        
        moves = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        visited = set()
        level = 1
        if count_fresh == 0:
            return 0

        while queue:
            len_level = len(queue)

            for _ in range(len_level):
                r, c = queue.popleft()
                visited.add((r, c))

                for a, b in moves:
                    if not inbound(r+a, c+b) or (r+a, c+b) in visited:
                        continue
                    if grid[r+a][c+b] == 1:
                        grid[r+a][c+b] = 2
                        queue.append((r+a, c+b))
                        count_fresh -= 1
                        if count_fresh == 0:
                            return level
            level += 1
        return -1