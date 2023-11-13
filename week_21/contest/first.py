def solve():
    m = int(input())
    arr = []
    for i in range(10):
        arr.append(10 ** i)
    ans = float("inf")
    for num in arr:
        if num > m:
            break
        ans = min(ans, abs(m - num))
    print(ans)

t = int(input())
for _ in range(t):
    solve()