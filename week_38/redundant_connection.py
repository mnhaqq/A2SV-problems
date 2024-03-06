class UnionFind:
    def __init__(self, size):
        self.root = {i: i for i in range(size)}
        self.size = [1] * size

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.size[rootX] > self.size[rootY]:
                self.root[rootY] = rootX
            elif self.size[rootX] < self.size[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.size[rootX] += 1


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = UnionFind(len(edges))

        for a, b in edges:
            if dsu.find(a-1) == dsu.find(b-1):
                return [a, b]
            dsu.union(a-1, b-1)
        return []
