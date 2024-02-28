class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None for _ in range(26)]

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            val = ord(c) - ord('a')
            if curr.children[val] == None:
                curr.children[val] = TrieNode()
            curr = curr.children[val]   
        curr.is_end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            val = ord(c) - ord('a')
            if curr.children[val] == None:
                return False
            curr = curr.children[val]
        return curr.is_end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            val = ord(c) - ord('a')
            if not curr.children[val]:
                return False
            curr = curr.children[val]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
