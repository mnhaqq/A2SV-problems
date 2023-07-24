def solve():
    n=int(input())
    a=list(map(int, input().split()))
    ops=0
    i=0
    while i < n:
        if a[i]<0:
            ops+=1
            while i<n and a[i]<=0:
                a[i]=a[i]*-1
                i+=1
        i+=1
    print(sum(a),ops)

t=int(input())
for _ in range(t):
    solve()