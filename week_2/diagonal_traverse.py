class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        len_mat = len(mat)
        len_row = len(mat[0])
        mat_size = len_mat*len_row
        out = []
        i = j = 0

        while len(out) < mat_size:
            #move diagonal up
            while i >= 0 and j < len_row and len(out) < mat_size:
                out.append(mat[i][j])
                i-=1
                j+=1
            # print(out)
            i+=1
            j-=1

            if j == len_row-1:
                i+=1
            else:
                j+=1

            #move diagonal down
            while j >= 0 and i < len_mat and len(out) < mat_size:
                out.append(mat[i][j])
                j-=1
                i+=1
            # print(out)
            j+=1
            i-=1

            if i == len_mat-1:
                j+=1
            else:
                i+=1
        return out