class Solution:
    def customSortString(self, order: str, s: str) -> str:
        dic = Counter(s)
        
        ans = ''
        for c in order:
            if c in dic:
                ans += (c * dic[c])
                del dic[c]
        for a, b in dic.items():
            ans += (a * b)
        return ans
