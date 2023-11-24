def solve():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    ans = float("-inf")
    a = [0] + a
    for i in range(len(a)-1):
        ans = max(ans, a[i+1]-a[i])
    ans = max(ans, 2*(x - a[-1]))
    print(ans)

t = int(input())
for _ in range(t):
    solve()