class Solution:
    def __init__(self):
        self.root = {}

    def add_word(self, word):
        curr = self.root
        for c in word:
            if c not in curr:
                curr[c] = {}

            if "count" not in curr:
                curr["count"] = 1
            else:
                curr["count"] += 1
            curr = curr[c]
        if "count" not in curr:
            curr["count"] = 1
        else:
            curr["count"] += 1
        curr["#"] = {}

    def calc_score(self, word):
        curr = self.root
        score = 0

        for c in word:
            curr = curr[c]
            if "count" in curr:
                score += curr["count"]
        return score

    def sumPrefixScores(self, words: List[str]) -> List[int]:
        for word in words:
            self.add_word(word)

        del self.root['count']
        
        ans = [0] * len(words)
        for i in range(len(words)):
            ans[i] = self.calc_score(words[i])
        
        return ans
