def solve():
    n = int(input())
    x = list(map(int, input().split()))

    x.sort()
    
    pr_sum = [1]
    for i in range(len(x)):
        if x[i] <= pr_sum[i]:
            pr_sum.append(pr_sum[i] + x[i])
        else:
            print(pr_sum[i])
            return
    print(pr_sum[-1])
    
solve()