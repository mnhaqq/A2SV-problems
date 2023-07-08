def solve():
    n=int(input())
    a=list(map(int, input().split()))
    b=list(map(int, input().split()))

    a.sort()
    b.sort()
    for i in range(n):
        if a[i] !=b[i] and a[i]+1 != b[i]:
            print("NO")
            return
    print("YES")

t = int(input())
for _ in range(t):
    solve()