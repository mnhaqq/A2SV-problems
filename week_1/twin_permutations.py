def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    a = [[j, i] for i, j in enumerate(a)]
    a.sort()
    possible = list(reversed(range(1, n+1)))

    b = [0] * (n+1)
    for i in range(len(a)):
        b[a[i][1]] = possible[i]
    b.pop()
    print(*b)
    

t = int(input())
for _ in range(t):
    solve()