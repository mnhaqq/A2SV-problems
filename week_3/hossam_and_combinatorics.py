def solve():
    n = int(input())
    a = list(map(int, input().split()))
    maximum = max(a)
    minimum = min(a)
    if maximum == minimum:
        print(n*(n-1))
        return
    print(a.count(minimum)*(2*a.count(maximum)))

t = int(input())
for _ in range(t):
    solve()