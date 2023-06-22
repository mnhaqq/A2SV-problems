class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_indexes = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zero_indexes.append((i, j))

        for index in zero_indexes:
            for i in range(len(matrix)):
                if index[0] == i:
                    for j in range(len(matrix[0])):
                        matrix[i][j] = 0
                for j in range(len(matrix[0])):
                    if index[0] == i and index[1] == j:
                        for i in range(len(matrix)):
                            matrix[i][j] = 0
                            