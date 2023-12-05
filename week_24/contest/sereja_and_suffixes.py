def solve():
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))

    suffix = set()
    res = []

    for num in reversed(nums):
        suffix.add(num)
        res.append(len(suffix))
    res.reverse()

    for i in range(m):
        q = int(input())
        print(res[q-1])

solve()