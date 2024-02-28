class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        curr["#"] = {}

    def search(self, word: str) -> bool:

        def dfs(node, i):
            if i == len(word):
                return "#" in node
            
            if word[i] != ".":
                return word[i] in node and dfs(node[word[i]], i+1)
    
            for c in node.keys():
                if dfs(node[c], i+1):
                    return True
            return False
            
        return dfs(self.root, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
