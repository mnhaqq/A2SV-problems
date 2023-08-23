def solve():
    n=int(input())
    b = list(map(int, input().split()))
    l = 0
    r = n-1
    out = []
    while l <= r:
        out.append(b[l])
        if l != r:
            out.append(b[r])
        l+=1
        r-=1
    print(*out)

t=int(input())
for _ in range(t):
    solve()