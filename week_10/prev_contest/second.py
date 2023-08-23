def solve():
    n = int(input())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))

    biggest = out = 0
    for i in range(len(matrix)):
        if matrix[i][0] <= 10 and matrix[i][1] > biggest:
            biggest = matrix[i][1]
            out = i+1
    print(out)

t=int(input())
for _ in range(t):
    solve()