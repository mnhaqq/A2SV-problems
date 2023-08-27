def solve():
    n = int(input())
    v = list(map(int, input().split()))
    m = int(input())
    questions = [list(map(int, input().split())) for i in range(m)]
 
    sorted_v = sorted(v)
    sum_v = sum(v)
    pr_sum_v = [0]
    pr_sum = 0
    for i in range(n):
        pr_sum+=v[i]
        pr_sum_v.append(pr_sum)

    pr_sum_sorted_v=[0]
    pr_sum = 0
    for i in range(n):
        pr_sum+=sorted_v[i]
        pr_sum_sorted_v.append(pr_sum)

    answer = []
    for i in range(m):
        q_type = questions[i][0]
        l = questions[i][1]
        r = questions[i][2]

        if q_type == 1:
            ans = pr_sum_v[r]-pr_sum_v[l-1]
        else:
            ans = pr_sum_sorted_v[r]-pr_sum_sorted_v[l-1]
        print(ans)     
 
solve()