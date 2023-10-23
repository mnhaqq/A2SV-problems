def solve():
    n = int(input())
    a = list(map(int, input().split()))

    ans = longest = 1
    for i in range(len(a)-1):
        if a[i] < a[i+1]:
            longest += 1
        else:
            ans = max(ans, longest)
            longest = 1
    ans = max(longest, ans)
    print(ans)


solve()