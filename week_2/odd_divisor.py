def solve():
    n = int(input())
    for i in range(50):
        if (2**i) == n:
            print("NO")
            return
    print("YES")
    
t = int(input())
for _ in range(t):
    solve()