class WordFilter:

    def __init__(self, words: List[str]):
        self.root = {}

        def add_word(word, word_idx):
            curr = self.root
            for c in word:
                if c not in curr:
                    curr[c] = {}
                curr['idx'] = word_idx
                curr = curr[c]
            curr['idx'] = word_idx
                

        for i in range(len(words)):
            for j in range(len(words[i])):
                add_word(words[i][j:] + '#' + words[i], i)

    def find_word(self, word):
        curr = self.root
        for c in word:
            if c not in curr:
                return -1
            curr = curr[c]
        return curr['idx']
        
        
    def f(self, pref: str, suff: str) -> int:
        word = suff + '#' + pref
        return self.find_word(word)



# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)
