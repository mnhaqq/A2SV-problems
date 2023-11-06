def solve():
    n, h = map(int, input().split())
    a = list(map(int, input().split()))

    def check(n):
        num = n
        for i in range(len(a) - 1):
            num += n
            if a[i] + n > a[i+1]:
                num -= n
                num += a[i+1] - a[i]
        if num >= h:
            return True
        return False

    ans = float("inf")
    low, high = 0, h
    while low <= high:
        mid = (low + high) // 2
        if check(mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    print(ans)


t = int(input())
for _ in range(t):
    solve()