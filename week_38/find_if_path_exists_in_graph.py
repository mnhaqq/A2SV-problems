class UnionFind:
    def __init__(self, n):
        self.root = {i: i for i in range(n)}
        self.size = [1] * n

    def find(self, node):
        root = node
        while root != self.root[root]:
            root = self.root[root]

        while node != root:
            parent = self.root[node]
            self.root[node] = root
            node = parent
            
        return root
    
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
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        dsu = UnionFind(n)

        for a, b in edges:
            dsu.union(a, b)

        return dsu.find(source) == dsu.find(destination)
