def solve():
    a , b = map(int, input().split())
    low, high = 0, (a+b)//4
    ans = 0
    while low <= high:
        mid = (high + low) // 2
        if a+b >= 4*mid and a >= mid and b >= mid:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    print(ans)

t = int(input())
for _ in range(t):
    solve()