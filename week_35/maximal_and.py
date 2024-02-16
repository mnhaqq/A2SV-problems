def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    j = 30
    while j >= 0 and k > 0:
        count = 0
        for i in range(n):
            if (a[i] & (1 << j)) == 0:
                count += 1
        
        if count <= k:
            for i in range(n):
                a[i] = a[i] | (1 << j)
            k -= count
        j -= 1

    ans = (2**31) - 1
    for i in range(n):
        ans = ans & a[i]
    print(ans)

t = int(input())
for _ in range(t):
    solve()