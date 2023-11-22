from collections import defaultdict

class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        dic = defaultdict(list)
        for u, v in edges:
            dic[u].append(v)
            if len(dic[u]) > 1:
                return u
            dic[v].append(u)
            if len(dic[v]) > 1:
                return v