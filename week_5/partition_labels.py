from collections import OrderedDict
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last=OrderedDict()
        for i in range(len(s)):
            last[s[i]]=i
        final=[]
        left=0
        right=last.get(s[0])
        while left<=right:
            if last.get(s[left])>right:
                right=last.get(s[left])
            if left==right:
                final.append(right+1-sum(final))
                if left<len(s)-1:
                    left=left+1
                    right=last.get(s[left])
                    continue
            left+=1
        return final