def solve():
    board = []
    n, m = map(int, input().split())
    for i in range(n):
        board.append(list(map(int, input().split())))

    maximal = 0
    for i in range(n):
        for j in range(m):
            first_diagonal = 0
            y = i
            z = j
            while y > 0 and z > 0:
                y -= 1
                z -= 1
            while y < n and z < m:
                first_diagonal += board[y][z]
                y += 1
                z += 1
            
            second_diagonal = 0
            y = i
            z = j
            while y > 0 and z < m - 1:
                y -= 1
                z += 1
            while z >= 0 and y < n:
                second_diagonal += board[y][z]
                z -= 1
                y += 1

            p_sum = first_diagonal + second_diagonal - board[i][j]
            maximal = max(p_sum, maximal)
    print(maximal)

t = int(input())
for _ in range(t):
    solve()