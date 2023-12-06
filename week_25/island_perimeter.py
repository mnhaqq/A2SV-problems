class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        def inbound(r, c):
            return (0 <= r < len(grid) and 0 <= c < len(grid[0]))
        
        def dfs(r, c):
            nonlocal perimeter
            if (r, c) in visited:
                return
            if not inbound(r, c) or grid[r][c] == 0:
                perimeter += 1
                return
            visited.add((r, c))
            moves = [(-1, 0), (0, -1), (0, 1), (1, 0)]
            for a, b in moves:
                dfs(r+a, c+b)

        visited = set()
        perimeter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    dfs(i, j)
                    break
        return perimeter