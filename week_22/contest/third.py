def solve():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))

    l = r = window = 0
    while r < k:
        window += h[r]
        r += 1
    ans = l + 1
    min_window = window

    while r < n:
        window += h[r]
        window -= h[l]
        l += 1
        r += 1
        if window < min_window:
            ans = l + 1
            min_window = window
            
    print(ans)

solve()