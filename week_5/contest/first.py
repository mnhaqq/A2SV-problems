def solve():
    n=int(input())
    a=list(map(int, input().split()))
    a.sort()
    l=0
    r=n-1
    cost=0
    while l<r:
        cost+=a[r]-a[l]
        r-=1
        l+=1
    print(cost)

t=int(input())
for _ in range(t):
    solve()