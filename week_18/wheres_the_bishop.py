def solve():
    matrix = []
    for i in range(9):
        row = list(input())
        if i != 0:
            matrix.append(row)
    for row in matrix:
        print(row)


t = int(input())
for _ in range(t):
    solve()