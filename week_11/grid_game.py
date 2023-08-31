class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        #suffix sum for row 1
        suffix_sum = [0] * (len(grid[0])+2)
        for i in range(len(suffix_sum)-2, 0, -1):
            suffix_sum[i] = suffix_sum[i+1] + grid[0][i-1]
        
        #prefix sum for row 2
        prefix_sum = [0] * (len(grid[1])+2)
        for i in range(1, len(prefix_sum)-1):
            prefix_sum[i] = prefix_sum[i-1] + grid[1][i-1]
        
        #get best answer from possible answers
        possible_answers = []
        for i in range(1, len(suffix_sum)-1):
            possible_answers.append(max(suffix_sum[i+1], prefix_sum[i-1]))
        return min(possible_answers)