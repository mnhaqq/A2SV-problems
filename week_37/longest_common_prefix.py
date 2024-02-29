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

    def longestCommonPrefix(self, strs: List[str]) -> str:
        for word in strs:
            self.add_word(word)
        
        def dfs(node, prefix):
            if len(node) > 1:
                return prefix
            if len(node) == 1 and list(node.keys())[0] != "#":
                key = list(node.keys())[0]
                prefix += key
                return dfs(node[key], prefix)
            return prefix

        if len(self.root) > 1 or (len(self.root) == 1 and list(self.root.keys())[0] == "#"):
            return ""
        return dfs(self.root, "")
