def solve():
    n = int(input())
    h = list(map(int, input().split()))

    h.append(0)
    for i in range(n):
        h[i+1] += h[i]-i
        
    for i in range(n):
        if h[i] < i:
            print("NO")
            return
    print("YES")

t = int(input())
for _ in range(t):
    solve()