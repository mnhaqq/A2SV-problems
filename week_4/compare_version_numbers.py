class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split(".")
        version2 = version2.split(".")
        version1 = [int(i) for i in version1]
        version2 = [int(i) for i in version2]
        max_len = max(len(version1), len(version2))
        while len(version1) < max_len:
            version1.append(0)
        while len(version2) < max_len:
            version2.append(0)
        
        pointer1=pointer2=0
        while pointer1 < max_len and pointer2 < max_len:
            if version1[pointer1] < version2[pointer2]:
                return -1
            elif version1[pointer1] > version2[pointer2]:
                return 1
            pointer1+=1
            pointer2+=1
        return 0