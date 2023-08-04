class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        pointer_t=pointer_s=0
        while pointer_t<len(t):
            target=t[pointer_t]
            status=False
            while pointer_s<len(s):                
                if s[pointer_s]==target:
                    status=True
                    pointer_s+=1
                    break
                pointer_s+=1
            if not status:
                return len(t)-pointer_t
            pointer_t+=1
        return 0