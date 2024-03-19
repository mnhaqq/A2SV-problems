def solve():
    n = int(input())
    a = list(map(int, input().split()))
    ans = [n+1 - a[i] for i in range(n)]
    print(*ans)

t = int(input())
for _ in range(t):
    solve()
