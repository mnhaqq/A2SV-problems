class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        def dfs(r, c):
            if r < 0 or r > len(grid)-1 or c < 0 or c > len(grid[0])-1:
                return
            if grid[r][c] == "0" or check[r][c]:
                return
            check[r][c] = True
            moves = [(0,-1), (-1,0), (1,0), (0,1)]
            for a, b in moves:
                dfs(r+a, c+b)

        check = [[False] * len(grid[0]) for _ in range(len(grid))]
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "0" or check[i][j]:
                    continue
                count += 1
                dfs(i, j)
        
        return count