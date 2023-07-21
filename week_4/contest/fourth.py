def solve():
    s=input()
    n=len(s)
    last_one=last_two=last_three=-1
    l=ans=float("inf")

    for r in range(n):
        if s[r]=="1":
            last_one=r
        elif s[r]=="2":
            last_two=r
        else:
            last_three=r
        if last_one!=-1 and last_two!=-1 and last_three!=-1:
            l=min(last_one, last_two, last_three)
            ans=min(ans, r-l+1)
    if ans==float("inf"):
        ans=0
    print(ans)


t=int(input())
for _ in range(t):
    solve()