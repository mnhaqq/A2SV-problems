from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans = [-1, -1]
        len_window = float('inf')
        
        dic_t = Counter(t)
        dic_s = Counter()
        
        l = 0
        for r in range(len(s)):
            dic_s[s[r]] += 1
    
            while dic_s & dic_t == dic_t:
                dic_s[s[l]] -= 1

                if r - l < len_window:
                    ans[0], ans[1] = l, r
                    len_window = r - l
                
                l += 1
            
                
        if ans == [-1, -1]:
            return ""
        return s[ans[0]:ans[1]+1]