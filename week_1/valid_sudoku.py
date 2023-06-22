class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check row
        for row in board:
            for element in row:
                if element.isdigit() and row.count(element) > 1:
                        return False

        #check column
        for i in range(len(board[0])):
                tmp = []
                for j in range(len(board)):
                        tmp.append(board[j][i])
                for element in tmp:
                        if element.isdigit() and tmp.count(element) > 1:
                                return False 

        #check 3x3 sub boxes
        horizontal = 1
        i = 0
        num_checked = 0
        while num_checked < len(board):
                i = 0

                sub_box = []
                while i < len(board):
                        j = num_checked
                        while j < 3*horizontal:
                                sub_box.append(board[i][j])
                                j+=1
                        i+=1

                        if i % 3 == 0:
                                for element in sub_box:
                                        if element.isdigit() and sub_box.count(element) > 1:
                                                return False
                                sub_box = []
                horizontal+=1 
                num_checked+=3
        return True