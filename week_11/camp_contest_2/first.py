n, q = map(int, input().split())
p = list(map(int, input().split()))
matrix = []
for i in range(q):
    matrix.append(list(map(int, input().split())))

p.sort()
pr_sum = [0] * (len(p)+1)
pr_sum[0] = pr_sum[-1]
for i in range(1, len(pr_sum)):
    pr_sum[i] = pr_sum[i-1] + p[i-1]

for i in range(len(matrix)):
    ans = pr_sum[-1] - pr_sum[-1-matrix[i][0]]
    diff = pr_sum[-1] - pr_sum[-1-(matrix[i][0]-matrix[i][1])]
    ans -= diff
    print(ans)