class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        arr = []
        dic = dict()
        def helper(row, col):
            if (row, col) in dic:
                return dic[(row,col)]
            if row == 0 or col == 0 or col == row:
                return 1
            ans1 = helper(row-1,col-1)
            ans2 = helper(row-1, col)
            dic[(row-1,col-1)]  = ans1
            dic[(row-1, col)] = ans2
            return ans1 + ans2


        for col in range(rowIndex+1):
            ans = helper(rowIndex, col)
            arr.append(ans)
        return arr