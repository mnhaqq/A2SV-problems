class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p)>len(s):
            return []
        tmp=list(set(s))
        dic=dict()
        for i in range(len(tmp)):
            dic[tmp[i]]=0
        window=dic.copy()
        for i in range(len(p)):
            dic[p[i]]=dic.get(p[i],0)+1

        for i in range(len(p)):
            window[s[i]]=window.get(s[i],0)+1
        
        anagrams=[]
        if window==dic:
            anagrams.append(0)
        for r in range(len(p),len(s)):
            l=r-len(p)
            window[s[r]]+=1
            window[s[l]]-=1
            if window==dic:
                anagrams.append(l+1)
        return anagrams