class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:
        moves = [(1,0), (0,1), (-1,0), (0,-1)]
        visited = set()

        def inbound(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])
        
        def dfs(pos):
            nonlocal status
            nonlocal land_count

            land_count += 1
            r, c = pos
            if not inbound(r, c):
                status = status and False
                return
            if grid[r][c] == 0:
                return
            visited.add((r, c))

            for a, b in moves:
                if not inbound(r+a, c+b):
                    status = status and False
                    continue
                if grid[r+a][c+b] == 0 or (r+a, c+b) in visited:
                    continue
                dfs((r+a, c+b))

        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0 or (i, j) in visited:
                    continue
                status = True
                land_count = 0
                dfs((i, j))
                if status:
                    ans += land_count
        return ans