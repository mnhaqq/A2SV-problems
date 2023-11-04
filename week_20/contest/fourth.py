def solve():
    n = int(input())
    a = list(map(int, input().split()))

    longest = 1
    tmp = 1
    for i in range(1, len(a)):
        if a[i] >= a[i-1]:
            tmp += 1
        else:
            longest = max(longest, tmp)
            tmp = 1
    longest = max(longest, tmp)
    print(longest)
solve()