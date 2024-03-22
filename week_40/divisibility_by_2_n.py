def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    idx = []
    nums = []
    def check(n):
        ans = 0
        while n % 2 == 0:
            ans += 1
            n = n // 2
        return ans
        
    for i in range(n):
        idx.append(check(i+1))
        nums.append(check(a[i]))
    
    s = sum(nums)
    if s >= n:
        print(0)
        return
    idx.sort(reverse=True)
    
    ans = 0
    for i in range(n):
        ans += 1
        s += idx[i]
        if s >= n:
            print(ans)
            return
    print(-1)


t = int(input())
for _ in range(t):
    solve()
