class Solution:
    def nextGreaterElement(self, n: int) -> int:
        n = list(str(n))
        i = len(n) - 2
        
        while i >= 0 and n[i] >= n[i+1]:
            i -= 1
        if i == -1:
            return -1
        
        j = len(n) - 1
        while i < j and n[j] <= n[i]:
            j -= 1
        
        n[i], n[j] = n[j], n[i]
        n[i+1:] = sorted(n[i+1:])
        res = int("".join(n))
        if res < 2**31:
            return res
        return -1