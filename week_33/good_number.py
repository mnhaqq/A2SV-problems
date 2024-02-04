def solve():
    n, k = map(int, input().split())
    a = []
    for _ in range(n):
        a.append(input())
    
    ans = 0
    for num in a:
        check = set()
        for dig in num:
            if int(dig) <= k:
                check.add(dig)
        if len(check) == (k+1):
            ans += 1
    print(ans)
    
solve()