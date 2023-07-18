def solve():
    n=int(input())
    b=list(map(int, input().split()))

    final=[]
    left=0
    right=len(b)-1
    while left<=right:
        final.append(b[left])
        if left!=right:
            final.append(b[right])
        left+=1
        right-=1
    print(*final)

t=int(input())
for _ in range(t):
    solve()