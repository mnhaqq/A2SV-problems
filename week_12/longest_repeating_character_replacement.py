class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        len_s = len(s)
        dic = dict()
        l = longest = 0
        for r in range(len_s):
            dic[s[r]] = dic.get(s[r], 0) + 1
            if (r-l+1) - max(dic.values()) <= k:
                longest = max(longest, r-l+1)
            else:
                dic[s[l]] -= 1
                l+=1
        return longest