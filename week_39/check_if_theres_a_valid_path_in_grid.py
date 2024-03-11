class UnionFind:
    def __init__(self, grid):
        self.root = {}
        self.size = {}

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                self.root[(i,j)] = (i,j)
                self.size[(i,j)] = 1

    def find(self, root):
        member = root
        while root != self.root[root]:
            root = self.root[root]

        while member != root:
            parent = self.root[member]
            self.root[member] = root
            member = parent
        return root

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.size[rootX] > self.size[rootY]:
                self.root[rootY] = rootX
                self.size[rootX] += self.size[rootY]

            else:
                self.root[rootX] = rootY
                self.size[rootY] += self.size[rootX]

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        def inbound(r, c):
            return 0 <= r < m and 0 <= c < n

        dsu = UnionFind(grid)

        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    if inbound(i, j-1) and (grid[i][j-1] in (1, 4, 6)):
                        dsu.union((i, j-1), (i, j))
                    if inbound(i, j+1) and (grid[i][j+1] in (1, 3, 5)):
                        dsu.union((i, j), (i, j+1))

                elif grid[i][j]==2:
                    if inbound(i-1, j) and (grid[i-1][j] in (2, 3, 4)):
                        dsu.union((i-1, j), (i, j))
                    if inbound(i+1, j) and grid[i+1][j] in (2, 5, 6):
                        dsu.union((i, j), (i+1, j))

                elif grid[i][j]==3:
                    if inbound(i, j-1) and (grid[i][j-1] in (1, 4, 6)):
                        dsu.union((i, j-1), (i, j))
                    if inbound(i+1, j) and (grid[i+1][j] in (2, 5, 6)):
                        dsu.union((i, j), (i+1, j))

                elif grid[i][j]==4:
                    if inbound(i, j+1) and (grid[i][j+1] in (1, 3, 5)):
                        dsu.union((i, j+1), (i, j))
                    if inbound(i+1, j) and (grid[i+1][j] in (2, 5, 6)):
                        dsu.union((i, j), (i+1, j))

                elif grid[i][j]==5:
                    if inbound(i, j-1) and (grid[i][j-1] in (1, 4, 6)):
                        dsu.union((i, j-1), (i, j))
                    if inbound(i-1, j) and (grid[i-1][j] in (2, 3, 4)):
                        dsu.union((i, j), (i-1, j))

                else:
                    if inbound(i, j+1) and (grid[i][j+1] in (1, 3, 5)):
                        dsu.union((i, j+1), (i, j))
                    if inbound(i-1, j) and (grid[i-1][j] in (2, 3, 4)):
                        dsu.union((i, j), (i-1, j))

        return dsu.find((m-1, n-1))==dsu.find((0, 0))
