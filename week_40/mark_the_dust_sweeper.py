def solve():
    n = int(input())
    a = list(map(int, input().split()))

    ans = 0
    flag = False
    for i in range(n-1):
        if a[i] != 0:
            flag = True
            ans += a[i]
        elif flag:
            ans += 1
    print(ans)

t = int(input())
for _ in range(t):
    solve()
