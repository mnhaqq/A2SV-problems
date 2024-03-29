def solve():
    n = int(input())
    l = 2 * n
    for i in range(l):
        for j in range(n):
            if (i // 2 + j) % 2 == 0:
                print('##', end="")
            else:
                print('..', end="")
        print()

t = int(input())
for _ in range(t):
    solve()