def solve():
    n, c = map(int, input().split())
    a = list(map(int, input().split()))

    counter = [0]*(max(a)+1)
    for i in range(n):
        counter[a[i]]+=1

    total_cost = 0
    for i in range(len(counter)):
        if counter[i]==0:
            continue
        if c <= counter[i]:
            total_cost+=c
        elif counter[i]<c:
            total_cost+=counter[i]
    print(total_cost)

t = int(input())
for _ in range(t):
    solve()