def solve():
    n = int(input())

    f = s = t = 0
    
    while n > 0:
        f += 1
        n -= 1
        if s + 1 < f and n > 0:
            s += 1
            n -= 1
        if t + 1 < s and n > 0:
            t += 1
            n -= 1

    print(s, f, t)

t = int(input())
for _ in range(t):
    solve()