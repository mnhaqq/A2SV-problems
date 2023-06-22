class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                y = i
                z = j
                check = set()
                while y < len(matrix) and z < len(matrix[0]):
                    check.add(matrix[y][z])
                    y+=1
                    z+=1
                if len(check) > 1:
                    return False
        return True