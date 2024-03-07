class UnionFind:
    def __init__(self):
        self.root = {}
        for i in range(26):
            self.root[chr(ord('a')+i)] = chr(ord('a')+i)

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

        if rootX < rootY:
            self.root[rootY] = rootX
        else:
            self.root[rootX] = rootY


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        dsu = UnionFind()
        for i in range(len(s1)):
            dsu.union(s1[i], s2[i])

        ans = [dsu.find(i) for i in baseStr]
        return ''.join(ans)
