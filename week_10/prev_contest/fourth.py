def solve():
    n = int(input())
    L = list(map(int, input().split()))

    arr = [True] * n
    L = L[::-1]
    slow = 0
    fast = 1
    while fast < n:
        if L[slow] == 0:
            slow += 1
            if slow == fast:
                fast += 1
            continue
        while fast < n and abs(fast - slow) <= L[slow]:
            arr[fast] = False
            fast += 1
        slow += 1
    ans = arr.count(True)
    print(ans)

solve()