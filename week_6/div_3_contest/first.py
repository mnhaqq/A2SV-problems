def solve():
    n,m,k,H=map(int, input().split())
    h=list(map(int, input().split()))

    diff=[abs(i-H) for i in h]
    count=0
    for i in range(len(diff)):
        if diff[i]-(k-1)*m<m and diff[i]%k==0 and h[i]!=H   :
            count+=1
    print(count)

t=int(input())
for _ in range(t):
    solve()