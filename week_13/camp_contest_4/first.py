def solve():
    s = input()
    n = len(s)
    greatest = 0
    tmp = 1
    for i in range(1, n):
        if s[i-1] == s[i]:
            tmp += 1
        else: 
            tmp = 1
        greatest = max(greatest, tmp)
    if greatest >= 7:
        print("YES")
    else:
        print("NO")

solve()