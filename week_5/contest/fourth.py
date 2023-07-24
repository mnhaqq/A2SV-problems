def solve():
    n,c=input().split()
    n=int(n)
    s=input()
    s+=s
    if c=="g":
        print(0)
        return
    possible_cross=[]
    l=r=0
    while r<n*2:
        if s[l]!=c:
            l+=1
            r+=1
            continue
        if s[l]==c:
            while r<n*2 and s[r]!="g":
                possible_cross.append(r-l+1)
                r+=1
            while r<n*2 and s[r]=="g":
                r+=1
            l=r
        r+=1
    print(max(possible_cross))


t=int(input())
for _ in range(t):
    solve()