from collections import deque

class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        def inbound(r, c):
            return 0 <= r < len(mat) and 0 <= c < len(mat[0])
        
        moves = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        queue = deque()

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    mat[i][j] = -1
        
        while queue:
            r, c = queue.popleft()

            for a, b in moves:
                if inbound(r+a, c+b) and mat[r+a][c+b] == -1:
                    mat[r+a][c+b] = mat[r][c] + 1
                    queue.append((r+a, c+b))
        return mat
        
        
