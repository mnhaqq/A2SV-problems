def solve():
    s = input()
    a = s.count("A")
    b = s.count("B")
    if a > b:
        print("A")
    else:
        print("B")

t = int(input())
for _ in range(t):
    solve()