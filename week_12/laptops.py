def solve():
    n = int(input())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))

    matrix.sort(key=lambda x: x[1], reverse=True)
    for i in range(1, n):
        if matrix[i][0] > matrix[i-1][0]:
            print("Happy Alex")
            return
    print("Poor Alex")

solve()