def solve():
    n = int(input())
    s = "#" + input() + "#"

    for i in range(n):
        if s[i] == s[i-1] == s[i+1] == ".":
            print(2)
            return
    print(s.count("."))

t = int(input())
for _ in range(t):
    solve()