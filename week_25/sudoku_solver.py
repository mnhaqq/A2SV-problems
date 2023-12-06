class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isvalid(r, c, check):
            x = y = z = True
            for i in range(len(board)):
                #check current column
                x = board[i][c] != check
                #check current row
                y = board[r][i] != check
                #check 3x3
                z = board[3*(r//3) + i//3][3*(c//3) + i%3] != check
                if not x or not y or not z:
                    return False
            return True
             
        def inbound(a):
            return 0 <= a < 9

        def backtrack(r, c):
            if not inbound(r):
                return True
            if not inbound(c):
                return backtrack(r+1, 0)

            if board[r][c] == ".":
                for num in range(1, 10):
                    if isvalid(r, c, str(num)):
                        board[r][c] = str(num)
                        if backtrack(r, c+1):
                            return True
                        board[r][c] = "."
                return False
            return backtrack(r, c+1)

        backtrack(0, 0)