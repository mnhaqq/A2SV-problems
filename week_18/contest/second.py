def solve():
    n = int(input())
    a = list(map(int, input().split()))

    dic = dict()
    for i in range(len(a)):
        dic[a[i]] = dic.get(a[i], 0) + 1
        if dic[a[i]] > 1:
            print("NO")
            return
    print("YES") 

t = int(input())
for _ in range(t):
    solve()