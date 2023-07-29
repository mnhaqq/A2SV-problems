class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        alphabets="abcdefghijklmnopqrstuvwxyz"
        window=dict()
        target=dict()
        for i in range(len(alphabets)):
            window[alphabets[i]]=0
            target[alphabets[i]]=0
        for i in range(len(s1)):
            target[s1[i]]+=1
            window[s2[i]]+=1
        for r in range(len(s1), len(s2)):
            if target==window:
                return True
            window[s2[r]]+=1
            window[s2[r-len(s1)]]-=1
        if target==window:
            return True
        return False