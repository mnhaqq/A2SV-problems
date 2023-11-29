class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        def dfs(r, c):
            nonlocal ans
            nonlocal count
            if r < 0 or r > len(grid)-1 or c < 0 or c > len(grid[0])-1 or grid[r][c] == 0 or check[r][c]:
                ans = max(ans, count)
                return
                
            check[r][c] = True
            count += 1
            moves = [(0,-1), (-1,0), (1,0), (0,1)]
            for a, b in moves:
                dfs(r+a, c+b)

        check = [[False] * len(grid[0]) for _ in range(len(grid))]

        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0 or check[i][j]:
                    continue
                count = 0
                dfs(i, j)
        return ans