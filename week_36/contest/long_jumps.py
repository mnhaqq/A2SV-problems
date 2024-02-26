def solve():
    n = int(input())
    a = list(map(int, input().split()))

    dp = [-1] * n
    dp[-1] = a[-1]
    for i in range(n-2, -1, -1):
        dp[i] = a[i]
        if i + a[i] < n:
            dp[i] += dp[i + a[i]]
    print(max(dp))

t = int(input())
for _ in range(t):
    solve()