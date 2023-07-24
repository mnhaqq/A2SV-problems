def solve():
    matrix=[]
    for i in range(8):
        matrix.append(input())
    final=""
    for i in range(8):
        for j in range(8):
            if matrix[i][j]!=".":
                final+=matrix[i][j]
    print(final)

t=int(input())
for _ in range(t):
    solve()