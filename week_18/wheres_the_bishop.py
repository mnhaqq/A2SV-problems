def solve():
    matrix = []
    for i in range(9):
        row = list(input())
        if i != 0:
            matrix.append(row)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])-2):
            if matrix[i][j] == matrix[i][j+2] == "#":
                ans = [i+2, j+2]
                print(*ans)
                return  


t = int(input())
for _ in range(t):
    solve()