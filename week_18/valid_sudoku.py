class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        #check rows
        for i in range(len(board)):
            check = set()
            for j in range(len(board[0])):
                if board[i][j].isdigit() and board[i][j] in check:
                    return False
                check.add(board[i][j])

        #check columns
        for i in range(len(board[0])):
            check = set()
            for j in range(len(board)):
                if board[j][i].isdigit() and board[j][i] in check:
                    return False
                check.add(board[j][i])
        
        #check 3x3
        horizontal = 1
        i = 0
        while i < len(board):
            for r in range(len(board)):
                if r % 3 == 0:
                    check = set()
                for c in range(i, horizontal * 3):
                    if board[r][c].isdigit() and board[r][c] in check:
                        return False
                    check.add(board[r][c])
            i += 3
            horizontal += 1
        return True
                