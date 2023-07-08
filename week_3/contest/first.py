def solve():
    n=int(input())
    a = list(map(int, input().split()))
    maximum=max(a)
    minimum=min(a)
    print(a.index(minimum)+1, a.index(maximum)+1)

t = int(input())
for _ in range(t):
    solve()