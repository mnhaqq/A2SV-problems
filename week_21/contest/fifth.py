def solve():
    m = int(input())
    p = list(map(int, input().split()))
    
    def sort(arr):
        nonlocal count
        if len(arr) <= 1:
            return arr[:]

        left = sort(arr[:len(arr)//2])
        right = sort(arr[len(arr)//2:])

        if left[-1] > right[-1]:
            count += 1
            return right + left
        else:
            return left + right
    
    count = 0
    expected = list(sorted(p))
    ans = sort(p)
    if ans == expected:
        print(count)
    else:
        print(-1)

t = int(input())
for _ in range(t):
    solve()