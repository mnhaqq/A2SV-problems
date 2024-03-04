class Solution:
    def __init__(self):
        self.root = {}

    def add_word(self, word):
        curr = self.root
        for c in word:
            if c not in curr:
                curr[c] = {}

            curr = curr[c]
            if "count" not in curr:
                curr["count"] = 1
            else:
                curr["count"] += 1
        curr["#"] = {}

    def calc_score(self, word):
        score = 0

        curr = self.root
        for c in word:
            curr = curr[c]
            if "count" in curr:
                score += curr["count"]
        return score

    def sumPrefixScores(self, words: List[str]) -> List[int]:
        for word in words:
            self.add_word(word)
        
        ans = [0] * len(words)
        for i in range(len(words)):
            ans[i] = self.calc_score(words[i])
        return ans
