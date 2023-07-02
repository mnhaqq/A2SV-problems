def solve():
    arr = list(map(int, input().split()))
    arr.sort()
    distance = abs(arr[0]-arr[1]) + abs(arr[1]-arr[2]) + abs(arr[0]-arr[2])
    if distance < 4:
        print(0)
        return
    else:
        print(distance-4)

t = int(input())
for _ in range(t):
    solve()