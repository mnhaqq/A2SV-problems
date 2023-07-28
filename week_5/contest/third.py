def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    min_val=min(a)
    min_idx=a.index(min_val)

    #values to both right and left of minimum must both be increasing
    l=min_idx
    r=min_idx+1
    while l>0 or r<n:
        if l>0:
            if a[l-1]<a[l]:
                print("NO")
                return
        if r<n:
            if a[r-1]>a[r]:
                print("NO")
                return
        l-=1
        r+=1
    print("YES")
    
t=int(input())
for _ in range(t):
    solve()