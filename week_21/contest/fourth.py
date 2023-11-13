def solve():
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))

    winners = []
    max_a = max(a)
    max_b = max(b)
    if max_a > max_b:
        winners.append("Alice") 
        winners.append("Alice")
    elif max_b > max_a:
        winners.append("Bob")
        winners.append("Bob")
    else:
        winners.append("Alice")
        winners.append("Bob")

    for name in winners:
        print(name)
        
t = int(input())
for _ in range(t):
    solve()