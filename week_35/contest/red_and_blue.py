def solve():
    n = int(input())
    r = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))

    a1 = a2 = 0
    r_s = 0
    for i in range(n):
        r_s += r[i]
        a1 = max(a1, r_s)
    
    r_s = 0
    for i in range(m):
        r_s += b[i]
        a2 = max(a2, r_s)
    print(a1 + a2)

t = int(input())
for _ in range(t):
    solve()