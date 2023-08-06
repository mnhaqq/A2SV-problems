def solve():
    n=int(input())
    s=input()
    l=r=0
    ans=""
    while r<n:
        if r!=l and s[l]==s[r]:
            ans+=s[l]
            r+=1
            l=r
        r+=1
    print(ans)

t=int(input())
for _ in range(t):
    solve()