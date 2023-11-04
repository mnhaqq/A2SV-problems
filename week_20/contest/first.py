def solve():
    k, r = map(int, input().split())

    i = 1
    while True:
        if (k * i) % 10 == r or (k * i) % 10 == 0:
            print(i)
            return
        i += 1

solve()