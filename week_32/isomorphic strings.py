class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashmap = dict()
        check_dup = set()

        for i in range(len(s)):
            if s[i] not in hashmap and t[i] not in check_dup:
                hashmap[s[i]] = t[i]
                check_dup.add(t[i])

            if hashmap.get(s[i], 0) != t[i]:
                return False
        return True