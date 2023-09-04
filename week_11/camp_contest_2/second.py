def solve():
    s = input()
    m = int(input())
    matrix = []
    for _ in range(m):
        matrix.append(list(map(int, input().split())))
    
    pr_sum = [0] * (len(s))
    for i in range(1, len(s)):
        pr_sum[i] = pr_sum[i-1]
        if s[i] == s[i-1]:
            pr_sum[i] += 1

    for i in range(m):
        l = matrix[i][0] - 1
        r = matrix[i][1] - 1
        ans = pr_sum[r] - pr_sum[l]
        print(ans)


if __name__ == "__main__":
    solve()