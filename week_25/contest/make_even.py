def solve():
    n = int(input())

    if n % 2 == 0:
        print(0)
        return
    
    n = str(n)
    if int(n[0]) % 2 == 0:
        print(1)
        return
    for i in range(1, len(n)):
        if int(n[i]) % 2 == 0:
            print(2)
            return
    print(-1)
    

t = int(input())
for _ in range(t):
    solve()