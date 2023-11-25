def solve():
    n = int(input())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))

    ans = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i == j:
                continue
            if matrix[i][0] == matrix[j][1]:
                ans += 1
    print(ans)

solve()