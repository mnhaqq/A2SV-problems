class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat)*len(mat[0]) != r*c:
            return mat

        new_mat = []
        tmp = []
        for row in mat:
            for element in row:
                tmp.append(element)
                if len(tmp) == c:
                    new_mat.append(tmp)
                    tmp = []
        return new_mat