class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def dfs(r, c):
            if r < 0 or r > len(image)-1 or c < 0 or c > len(image[0])-1:
                return
            if image[r][c] == color or image[r][c] != original_col:
                return 
            image[r][c] = color
            moves = [(0,-1), (-1,0), (1,0), (0,1)]
            for a, b in moves:
                dfs(r+a, c+b)
                
        original_col = image[sr][sc]
        dfs(sr, sc)
        return image