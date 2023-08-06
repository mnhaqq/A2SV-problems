def solve():
    n=int(input())
    a=list(map(int, input().split()))

    sorted_a=sorted(a)
    i=n-1
    while i>=0:
        if a[i]!=sorted_a[i]:
            print(sorted_a[i])
            return
        i-=1
    print(0)

t=int(input())
for _ in range(t):
    solve()