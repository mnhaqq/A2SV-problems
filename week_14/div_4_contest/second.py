def solve():
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()
    a[0] += 1
    ans = 1
    for i in range(len(a)):
        ans *= a[i]
    print(ans)

t = int(input())
for _ in range(t):
    solve()