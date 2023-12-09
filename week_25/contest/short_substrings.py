def solve():
    b = input()

    ans = b[0]
    for i in range(1, len(b)-1):
        if i % 2 == 0:
            ans += b[i]
    ans += b[-1]
    print(ans)

t = int(input())
for _ in range(t):
    solve()