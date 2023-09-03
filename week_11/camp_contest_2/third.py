def solve():
    n = int(input())
    r = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))

    pr_sum_r = [0] * (n+1)
    for i in range(1, len(pr_sum_r)):
        pr_sum_r[i] = pr_sum_r[i-1] + r[i-1]

    pr_sum_b = [0] * (m+1) 
    for i in range(1, len(pr_sum_b)):
        pr_sum_b[i] = pr_sum_b[i-1] + b[i-1]
    ans = max(pr_sum_b) + max(pr_sum_r)
    print(ans)       

t = int(input())
for _ in range(t):
    solve()