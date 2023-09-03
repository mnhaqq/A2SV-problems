def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    prev = 10**10
    for i in range(k-1, 0, -1):
        num = a[i]-a[i-1]
        if num > prev:
            print("NO")
            return
        prev = num

    if (n-k+1) * prev < a[0]:
        print("NO")
        return
    print("YES")

t = int(input())
for _ in range(t):
    solve()