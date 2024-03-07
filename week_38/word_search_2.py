class Solution:
    def __init__(self):
        self.root = {}

    def insert(self, word):
        curr = self.root

        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        curr['#'] = {}


    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def inbound(r, c):
            return 0 <= r < len(board) and 0 <= c < len(board[0])

        def backtrack(r, c, word, pos):
            if not inbound(r, c) or board[r][c] not in pos:
                return
            visited.add((r, c))

            pos = pos[board[r][c]]
            if '#' in pos:
                ans.add(word + board[r][c])
            
            for a, b in moves:
                if (r+a, c+b) not in visited:
                    backtrack(r+a, c+b, word+board[r][c], pos)

            visited.remove((r, c))

        for word in words:
            self.insert(word)

        moves = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        ans = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in self.root:
                    visited = set()
                    backtrack(i, j, "", self.root)  
    
        return list(ans)
