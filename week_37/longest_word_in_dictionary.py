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

    def longestWord(self, words: List[str]) -> str:
        for word in words:
            self.add_word(word)

        def dfs(node, prefix):
            if "#" not in node and node != self.root:
                return prefix[:-1]

            for key, val in node.items():
                check = dfs(node[key], prefix+key)
                if check:
                    valid_words.add(check)
        
        valid_words = set()
        dfs(self.root, "")
        if not valid_words:
            return ""
        check = len(max(valid_words, key=len))
        ans = []
        for word in valid_words:
            if len(word) == check:
                ans.append(word)
        return min(ans)

