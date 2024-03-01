class Solution:
    def __init__(self):
        self.root = {}
    
    def add_word(self, word):
        curr = self.root
        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        curr["#"] = {}

    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        self.add_word(s)
        memo_true = set()
        memo_false = set()

        ans = 0
        for word in words:
            if word in memo_true:
                ans += 1
                continue
            if word in memo_false:
                continue
            
            i = 0
            curr = self.root
            while curr:
                if word[i] in curr:
                    curr = curr[word[i]]
                    i += 1
                else:
                    key = list(curr.keys())[0]
                    curr = curr[key]
                if i == len(word):
                    memo_true.add(word)
                    ans += 1
                    break
            if i < len(word):
                memo_false.add(word)
        return ans
