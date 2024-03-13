class UnionFind:
    def __init__(self, n):
        self.root = {i:i for i in range(n)}
        self.size = [1] * n

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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        dsu = UnionFind(n)

        hashmap = {}
        for i in range(n):
            for j in range(1, len(accounts[i])):
                if accounts[i][j] in hashmap:
                    dsu.union(i, hashmap[accounts[i][j]])
                else:
                    hashmap[accounts[i][j]] = i
        
        email_grp = defaultdict(list)
        for key, val in hashmap.items():
            leader = dsu.find(val)
            email_grp[leader].append(key)

        ans = []
        for i, email in email_grp.items():
            name = accounts[i][0]
            ans.append([name] + sorted(email_grp[i]))
            
        return ans
