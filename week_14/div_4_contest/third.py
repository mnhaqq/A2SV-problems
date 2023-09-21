def solve():
    matrix = []
    for i in range(10):
        ls = list(input())
        matrix.append(ls)
    
    ans = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if (i == 0 or i == 9 or j == 0 or j == 9) and matrix[i][j] == "X":
                ans += 1
            elif (i == 1 or i == 8 or j == 1 or j == 8) and matrix[i][j] == "X":
                ans += 2
            elif (i==2 or i == 7 or j == 2 or j == 7) and matrix[i][j] == "X":
                ans += 3
            elif (i == 3 or i == 6 or j == 3 or j==6) and matrix[i][j] == "X":
                ans += 4
            elif (i == 4 or i == 5 or j == 4 or j == 5) and matrix[i][j] == "X":
                ans += 5
    print(ans)


t = int(input())
for _ in range(t):
    solve()