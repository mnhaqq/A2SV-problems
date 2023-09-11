def solve():
    s = input()
    n = len(s)
    l, r = 0, n-1
    ans = []
    while l < r:
        while l < r and s[l] == ")":
            l+=1
        while l < r and s[r] == "(":
            r-=1

        if l < r:
            ans.append(l+1)
            ans.append(r+1)
        l+=1
        r-=1

    ans.sort()
    if ans:
        print(1)
        print(len(ans))
        print(*ans)
    else:
        print(0)
        
        


solve()