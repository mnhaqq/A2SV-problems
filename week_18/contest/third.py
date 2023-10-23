def solve():
    n, k = map(int, input().split())
    s = input()

    count = float("inf")
    dic = {"B":0, "W":0}

    for r in range(k):
        dic[s[r]] += 1

    if dic["B"] == k:
        print(0)
        return
    
    l = 0
    for r in range(k, n):
        if dic["B"] == k:
            print(0)
            return
        count = min(count, dic["W"])
        dic[s[r]]+=1
        dic[s[l]]-=1
        l += 1
    count = min(count, dic["W"])
    print(count)


t = int(input())
for _ in range(t):
    solve()