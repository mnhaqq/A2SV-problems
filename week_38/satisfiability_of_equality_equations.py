class DisjointSet:
    def __init__(self):
        self.root = {}
        letters = string.ascii_lowercase
        for i in letters:
            self.root[i] = i
        self.size = [1] * 26

    def find(self, node):
        root = node
        while root != self.root[root]:
            root = self.root[root]

        while node != root:
            parent = self.root[node]
            self.root[node] = root
            node = parent

        return root

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            if self.size[ord(rootX) - ord('a')] > self.size[ord(rootY) - ord('a')]:
                self.root[rootY] = rootX
                self.size[ord(rootX) - ord('a')] += self.size[ord(rootY) - ord('a')]
            else:
                self.root[rootX] = rootY
                self.size[ord(rootY) - ord('a')] +=  self.size[ord(rootX) - ord('a')]


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        dsu = DisjointSet()

        for eqn in equations:
            if eqn[1] == '=':
                dsu.union(eqn[0], eqn[-1])
        for eqn in equations:
            if eqn[1] == '!' and dsu.find(eqn[0]) == dsu.find(eqn[-1]):
                return False
        return True
