def solve():
    s = input()
    out_of_position = 0
    if s[0] != "a":
        out_of_position += 1
    if s[1] != "b":
        out_of_position += 1
    if s[2] != "c":
        out_of_position += 1
    if out_of_position <= 2:
        print("YES")
    else:
        print("NO")

t = int(input())
for _ in range(t):
    solve()