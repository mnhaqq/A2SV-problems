class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        check=""
        i=j=0
        while i <len(t) and j<len(s):
            if t[i]==s[j]:
                check+=t[i]
                j+=1
            i+=1
        if check==s:
            return True
        else:
            return False