import math
def solve():
    x = int(input())
    a = [ int(i) for i in range(1, math.ceil(x**(1/3)))]
    l = 0
    r = len(a)-1
    while l <= r:
        if a[l]**3 + a[r]**3 ==x:
            print("YES")
            return
        elif a[l]**3 + a[r]**3 < x:
            l+=1
        else:
            r-=1
    print("NO")
t = int(input())
for _ in range(t):
    solve()