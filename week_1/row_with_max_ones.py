class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        max_row = max_count = 0
        for row in range(len(mat)):
            count = mat[row].count(1)
            if count > max_count:
                max_row, max_count = row, count

        return [max_row, max_count]