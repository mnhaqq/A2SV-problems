def solve():
    n = int(input())
    s = input()

    l, r = 0, n-1
    while l < r:
        if s[l] != s[r]:
            l+=1
            r-=1
        else:
            break
    print(r-l+1)

t = int(input())
for _ in range(t):
    solve()