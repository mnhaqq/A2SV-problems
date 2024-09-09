def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = [float('inf')] + a + [float('inf')]

    def dp(i, ops):
        if ops == k:
            return 0
        if i >= (n - 2):
            return min(a[i], a[i-1])
        
        arr = []
        if i - 1 >= 0:
            arr.append(a[i-1])
        if i + 1 < n:
            arr.append(a[i+1])
        arr.append(a[i])
        one = dp(i+1, ops+1) + min(arr)
        two = dp(i+1, ops)
        return min(one, two)
    
    ans = dp(0, 0)
    print(ans)

t = int(input())
for _ in range(t):
    solve()