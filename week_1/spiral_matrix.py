class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        spiral_matrix = []
        i = j = up = left = right = down = 0
        num_elements = len(matrix) * len(matrix[0])

        while len(spiral_matrix) < num_elements:
            up+=1
            while j < len(matrix[0]) - right and len(spiral_matrix) < num_elements:
                spiral_matrix.append(matrix[i][j])
                j+=1
            j-=1
            i+=1

            right+=1
            while i < len(matrix) - down and len(spiral_matrix) < num_elements:
                spiral_matrix.append(matrix[i][j])
                i+=1
            i-=1
            j-=1

            down+=1
            while j >= left and len(spiral_matrix) < num_elements:
                spiral_matrix.append(matrix[i][j])
                j-=1
            j+=1
            i-=1

            left+=1
            while i > up and len(spiral_matrix) < num_elements:
                spiral_matrix.append(matrix[i][j])
                i-=1
        return spiral_matrix