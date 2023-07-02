def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    for i in range(n-1):
        if a[i+1] >= a[i]:
            print("YES")
            return
    print("NO")

t = int(input())
for _ in range(t):
    solve()