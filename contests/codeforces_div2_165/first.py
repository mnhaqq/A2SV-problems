def solve():
    n = int(input())
    p = list(map(int, input().split()))

    for i in  range(n):
        if i+1 == p[p[i]-1]:
            print(2)
            return
    print(3)

t = int(input())
for _ in range(t):
    solve()