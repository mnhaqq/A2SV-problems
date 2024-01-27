class Solution:
    def addSpaces(self, s: str, spaces: list[int]) -> str:
        new_s = ""
        p1 = p2 = 0
        while p1 < len(s):
            if p2 < len(spaces) and p1 == spaces[p2]:
                new_s += " "
                p2 += 1
            else:
                new_s += s[p1]
                p1 += 1
        return new_s
            