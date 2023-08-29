def solve():
    n = int(input())
    a = list(map(int, input().split()))

    maxx = n
    minn = 1
    l = 0
    r = n-1
    while l < r:
        if a[l] == maxx or a[r] == maxx:            
            if a[l] == maxx:
                l+=1
            else:
                r-=1
            maxx-=1
        elif a[r] == minn or a[l] == minn:
            if a[r] == minn:
                r-=1
            else:
                l+=1
            minn+=1
        else:
            print(l+1, r+1)
            return
    print(-1)
    


t = int(input())
for _ in range(t):
    solve()