class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        dic=dict()
        longest=l=0
        for r in range(n):
            dic[s[r]]=dic.get(s[r],0)+1
            if dic.get(s[r])>1:
                while dic.get(s[r])>1:
                    dic[s[l]]-=1
                    l+=1
            longest=max(longest,r-l+1)
        return longest