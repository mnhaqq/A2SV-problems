def solve():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))

    l = ans = count = 0
    for r in range(n):
        count += a[r]

        while count > t:
            count -= a[l]
            l += 1
        ans = max(ans, r-l+1)
    print(ans)

solve()