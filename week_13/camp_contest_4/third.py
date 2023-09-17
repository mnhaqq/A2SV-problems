def solve():
    n = int(input())
    weights = list(map(int, input().split()))

    #calc prefix sum
    pr_sum = [0] * (len(weights)+1)
    for i in range(1, len(pr_sum)):
        pr_sum[i] = pr_sum[i-1] + weights[i-1]

    #calc suffix sum
    rev_weights = list(reversed(weights))
    suf_sum = [0] * (len(weights)+1)
    for i in range(1, len(suf_sum)):
        suf_sum[i] = suf_sum[i-1] + rev_weights[i-1]
    suf_sum = list(reversed(suf_sum))


    alice, bob = 1, len(suf_sum)-2
    most = 0
    while alice <= bob:
        if pr_sum[alice] < suf_sum[bob]:
            alice += 1
        elif suf_sum[bob] < pr_sum[alice]:
            bob -= 1
        else:
            most = alice + len(suf_sum) - bob - 1
            alice += 1
            bob -= 1

    print(most)

    

t = int(input())
for _ in range(t):
    solve()