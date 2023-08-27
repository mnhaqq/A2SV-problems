def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    count = 0
    l=r=0
    while r < n:
        count=0
        while l < n and a[l] == a[r]:
            count+=1
            if count == 3:
                print(a[r])
                return
            l+=1
        else:
            r = l
    print(-1)


t = int(input())
for _ in range(t):
    solve()