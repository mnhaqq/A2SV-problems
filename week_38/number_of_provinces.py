class UnionFind:
    def __init__(self, n):
        self.root = {i: i for i in range(n)}
        self.size = [1] * n

    def find(self, node):
        while node != self.root[node]:
            node = self.root[node]
        return node
    
    def union(self, node1, node2):
        rootX = self.find(node1)
        rootY = self.find(node2)

        if rootX != rootY:
            if self.size[rootX] > self.size[rootY]:
                self.root[rootY] = rootX
                self.size[rootX] += self.size[rootY]
            else:
                self.root[rootX] = rootY
                self.size[rootY] +=  self.size[rootX]

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        union_find = UnionFind(n)
        ans = 0

        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1 and union_find.find(i) != union_find.find(j): 
                    union_find.union(i, j)
                    ans += 1
                    
        return n - ans
