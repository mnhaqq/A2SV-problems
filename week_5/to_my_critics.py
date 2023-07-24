def solve():
    a,b,c=map(int, input().split())
    if a+b>=10 or b+c>=10 or a+c>=10:
        print("YES")
    else:
        print("NO")

t=int(input())
for _ in range(t):
    solve()