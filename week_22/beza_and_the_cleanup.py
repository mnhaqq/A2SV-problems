def solve():
    n, m, s, A, B = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort(reverse=True)
    b.sort(reverse=True)

    pr_sum_a = [0] * (n+1)
    for i in range(1, n+1):
        pr_sum_a[i] = pr_sum_a[i-1] + a[i-1]

    pr_sum_b = [0] * (m+1)
    for i in range(1, m + 1):
        pr_sum_b[i] = pr_sum_b[i-1] + b[i-1]

    ans = float("-inf")
    for i in range(len(a) + 1):
        low, high = 0, len(b)
        while low <= high:
            mid = (low + high) // 2
            total_weight = A * i + B * mid
            if total_weight <= s:
                ans = max(ans, pr_sum_a[i] + pr_sum_b[mid])
                low = mid + 1
            else:
                high = mid - 1
    print(ans)

solve()
