class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic_s = dict()
        dic_t = dict()

        for i in range(len(s)):
            dic_s[s[i]] = dic_s.get(s[i], 0) + 1

        for i in range(len(t)):
            dic_t[t[i]] = dic_t.get(t[i], 0) + 1
        
        if dic_s == dic_t:
            return True
        return False