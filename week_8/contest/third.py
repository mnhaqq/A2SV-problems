def is_even(n):
    if n%2==0:
        return True
    return False
 
def solve():
    n=int(input())
    a=list(map(int, input().split()))
    tmp=sorted(a)
    for i in range(n):
        if is_even(tmp[i])!=is_even(a[i]):
            print("NO")
            return
    print("YES")
 
 
t=int(input())
for _ in range(t):
    solve()