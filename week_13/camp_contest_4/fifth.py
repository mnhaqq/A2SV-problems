def solve():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))

    window = l = r = ans = 0
    while r < len(a):
        while r < len(a) and window <= t:
            window += a[r]
            if window > t:
                ans = max(ans, r-l)
                break
            ans = max(ans, r-l+1)
            r+=1
        while l <= r and window > t:
            window -= a[l]
            l+=1
        r+=1
    print(ans)



solve()