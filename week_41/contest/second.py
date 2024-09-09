def solve():
    n = int(input())
    arr = list(input().split() for _ in range(n))
    
    ans = curr = 0
    check = [False] * (10 ** 6 + 1)
    for a, b in arr:
        if a == "+":
            curr += 1
            check[int(b)] = True
            ans = max(ans, curr)
        else:
            if check[int(b)]:
                curr -= 1
                check[int(b)] = False
            else:
                ans += 1
    print(ans)
    
solve()