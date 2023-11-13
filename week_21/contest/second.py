def solve():
    n = int(input())
    a = list(map(int, input().split()))

    ans = l = window = 0
    for r in range(len(a)):
        window += a[r]
        while l <= r and window > 0:
            window -= a[l]
            l += 1
        ans = max(ans, r-l+1)
    ans = max(ans, r-l+1)
    print(ans)


t = int(input())
for _ in range(t):
    solve()