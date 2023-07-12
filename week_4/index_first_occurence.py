class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        indices = []
        if needle in haystack:
            indices.append(haystack.index(needle))

        if needle in haystack:
            haystack=" ".join(haystack)
            haystack=haystack.split()
            return min(indices)
        return -1