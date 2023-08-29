class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.pr_sum = [[0]*(len(matrix[0])+1) for i in range(len(matrix)+1)]
        for i in range(1, len(self.pr_sum)):
            for j in range(1, len(self.pr_sum[0])):
                self.pr_sum[i][j] = matrix[i-1][j-1] + self.pr_sum[i-1][j] + self.pr_sum[i][j-1] - self.pr_sum[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = self.pr_sum[row2+1][col2+1] + self.pr_sum[row1][col1] - self.pr_sum[row2+1][col1] - self.pr_sum[row1][col2+1]
        return ans


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)