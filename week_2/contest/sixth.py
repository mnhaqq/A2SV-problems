def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()

    segments = []
    for i in range(m-1):
        segments.append(abs(a[i+1]-a[i]-1))
    segments.append(abs(n-a[m-1])+(a[0]-1))
    segments.sort(reverse=True)

    num_infected = 0
    protected = 0
    while len(segments) > 0 and max(segments)>num_infected:
        removed = segments.pop(0)
        protected+=max(1, removed - 1 - num_infected)
        num_infected+=4
    print(n-protected)


t = int(input())
for _ in range(t):
    solve()