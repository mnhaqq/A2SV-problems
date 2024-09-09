def solve():
    s = input()

    ans = window = i = 0
    while i < len(s):
        if s[i] == '1':
            break
        i+=1

    start = i
    for i in range(start, len(s)):
        window += 1
        if s[i] == '0':
            ans += window
            window -= 1
    print(ans)


t = int(input())
for _ in range(t):
    solve()