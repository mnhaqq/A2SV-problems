class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.size = [1] * size
        
    def find(self, x):
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
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

def countComponents(n, edges):
    dsu = UnionFind(n)
    for a, b in edges:
        if dsu.find(a) != dsu.find(b):
            dsu.union(a, b)
    
    ans = set()
    for i in range(n):
        ans.add(dsu.find(i))
    return len(ans)


n = 5
edges = [[0,1],[1,2],[2,3],[3,4]]
print(countComponents(n, edges))
        