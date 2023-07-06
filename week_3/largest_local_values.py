class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        max_local = [[0 for i in range(n-2)] for j in range(n-2)]
        for i in range(n-2):
            for j in range(n-2):
                r,c = i,j
                value = grid[r][c]
                for y in range(i, r+3):
                    for z in range(j, c+3):
                        value=max(value, grid[y][z])
                # print("done")
                max_local[i][j] = value
            
        return max_local