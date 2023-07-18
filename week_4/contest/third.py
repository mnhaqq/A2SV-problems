def solve():
    s=input()
    s=" ".join(s)
    s=s.split()
    n=len(s)
    if n==1:
        print(s[0])
        return

    ans=[]
    if s[0]!=s[1]:
        ans.append(s[0])
    if s[-1]!=s[-2]:
        ans.append(s[-1])
    left=0
    right=0
    while right<n:
        if s[left]==s[right]:
            right+=1
        elif s[left]!=s[right]:
            if (right-left)%2!=0:
                ans.append(s[left])
            left=right
            right+=1
        if right==n:
            if (right-left)%2!=0:
                ans.append(s[left])

    ans=list(set(ans))
    ans.sort()
    ans="".join(ans)
    print(ans)

t=int(input())
for _ in range(t):
    solve()