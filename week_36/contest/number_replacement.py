def solve():
    n = int(input())
    a = list(map(int, input().split()))
    s = input()

    dic = dict()
    for i in range(n):
        if a[i] not in dic:
            dic[a[i]] = s[i]
    
    for i in range(n):
        if dic[a[i]] != s[i]:
            print("NO")
            return
    print("YES")

t = int(input())
for _ in range(t):
    solve()