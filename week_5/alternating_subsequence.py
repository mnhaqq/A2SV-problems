def solve():
    n=int(input())
    a=list(map(int, input().split()))
    pointer=0
    
    final=[]
    while pointer<n:
        tmp=float("-inf")
        #check negative range
        while pointer<len(a) and a[pointer]<0:
            tmp=max(tmp, a[pointer])
            pointer+=1
        if tmp==float("-inf"):
            final.append(0)
        else:
            final.append(tmp)

        #check positive range
        tmp=float("-inf")
        while pointer<len(a) and a[pointer]>0:
            tmp=max(tmp, a[pointer])
            pointer+=1
        if tmp==float("-inf"):
            final.append(0)
        else:
            final.append(tmp)
    print(sum(final))


t=int(input())
for _ in range(t):
    solve()