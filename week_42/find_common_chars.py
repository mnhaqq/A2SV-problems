from collections import defaultdict

class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        word = set(words[0])
        dic = defaultdict(int)
        ans = []

        for c in word:
            check = float('inf')
            for i in range(len(words)):
                check = min(check, words[i].count(c))
            ans += ([c] * check)
        return ans
