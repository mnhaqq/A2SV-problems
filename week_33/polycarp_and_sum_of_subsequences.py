def solve():
    arr = list(map(int, input().split()))

    a = arr[0]
    b = arr[1]
    c = arr[6] - (a+b)
    print(a, b, c)

t = int(input())
for _ in range(t):
    solve()