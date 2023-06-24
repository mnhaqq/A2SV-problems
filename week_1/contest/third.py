def solve():
    n, k = map(int, input().split())

    if n%2 == 0:
        print("YES")
    elif n%2 != 0 and k%2 != 0:
        print("YES")
    else:
        print("NO")

t = int(input())
for _ in range(t):
    solve()