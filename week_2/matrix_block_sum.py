class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        num_rows = len(mat)
        num_cols = len(mat[0])

        answer = [[0 for j in range(len(mat[0]))] for i in range(len(mat))]
        for i in range(num_rows):
            for j in range(num_cols):
                r = max(0, i-k)
                c = max(0, j-k)

                max_r = min(i+k, num_rows-1)
                max_c = min(j+k, num_cols-1)

                original_r = r
                original_c = c
                curr_idx = 0

                while r <= max_r:
                    c = original_c
                    while c <= max_c:
                        curr_idx+=mat[r][c]
                        c+=1
                    r+=1

                answer[i][j] = curr_idx
        return answer