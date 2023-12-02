def solve():
    s = input()
    sum = 0
    for i in range(len(s)):
        if i < 3:
            sum += int(s[i])
        else:
            sum -= int(s[i])
    if sum == 0:
        print("YES")
    else:
        print("NO")

t = int(input())
for _ in range(t):
    solve()