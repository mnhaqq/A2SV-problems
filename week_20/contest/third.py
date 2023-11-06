def solve():
    n, s = map(int, input().split())
    a = list(map(int, input().split()))

    l = window_sum = 0
    longest = float("inf")
    if sum(a) < s:
        print(-1)
        return

    for r in range(len(a)):
        window_sum += a[r]
        while window_sum > s:
            window_sum -= a[l]
            l+=1
        longest = min(longest, n + (l - r - 1))
    print(longest)

t = int(input())
for _ in range(t):
    solve()