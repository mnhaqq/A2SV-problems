class Solution:
    def countBattleships(self, board: list[list[str]]) -> int:
        def inbound(r, c):
            return 0 <= r < len(board) and 0 <= c < len(board[0])

        def dfs(pos):
            r, c = pos

            if not inbound(r, c) or (r, c) in visited:
                return
            if board[r][c] == '.':
                return
            visited.add((r,c))
            for a, b in moves:
                dfs((r+a, c+b))


        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = set()

        ans = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X' and (i, j) not in visited:
                    dfs((i, j))
                    ans += 1
        return ans
