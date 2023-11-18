def solve():
    n = int(input())
    s = input()

    points = 0
    check = set()

    for i in range(len(s)):
        if s[i] not in check:
            points += 2
        else:
            points += 1
        check.add(s[i])
    print(points)


t = int(input())
for _ in range(t):
    solve()