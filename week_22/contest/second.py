def solve():
    s = input()

    ans = count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            count = 1
        ans = max(count, ans)
    ans = max(count, ans)
    if ans < 7:
        print("NO")
    else:
        print("YES")

solve()