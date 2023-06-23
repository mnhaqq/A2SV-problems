class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        # create sub matrices
        count = 0
        sub_matrices = []
        for i in range(len(grid)-2):
            for j in range(len(grid[0])-2):
                sub_matrix = []
                sub_matrix.append(grid[i][j:j+3])
                sub_matrix.append(grid[i+1][j:j+3])
                sub_matrix.append(grid[i+2][j:j+3])

                status = True

                #check for distinct numbers from 1 to 9
                check = set()
                for row in sub_matrix:
                    for element in row:
                        check.add(element)
                if len(check) < 9 or max(check) != 9:
                    continue

                check_sum = sum(sub_matrix[0])
                # check row sums
                for row in sub_matrix:
                    if sum(row) != check_sum:
                        status = False
                        break
                if status == False:
                    continue
                #check column sums
                for y in range(len(sub_matrix[0])):
                    for z in range(len(sub_matrix)-2):
                        if (sub_matrix[z][y] + sub_matrix[z+1][y] + sub_matrix[z+2][y]) != check_sum:
                            status = False
                            break
                    if status == False:
                        break
                if status == False:
                    continue

                #check diagonals
                #check primary diagonal
                if (sub_matrix[0][0] + sub_matrix[1][1] + sub_matrix[2][2]) != check_sum:
                    status = False
                    continue

                #check secondary diagonal
                if (sub_matrix[0][2] + sub_matrix[1][1] + sub_matrix[2][0]) != check_sum:
                    status = False
                    continue

                if status == True:
                    count+=1

        return count