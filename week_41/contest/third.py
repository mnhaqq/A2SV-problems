def solve():
    r1, c1, r2, c2 = map(int, input().split())
    
    r = b = k = 0

    k = max(abs(r1 - r2), abs(c1 - c2))
    if r1 == r2 or c1 == c2:
        r = 1
    else:
        r = 2

    if (r1 + c1) % 2 != (r2 + c2) % 2:
        b = 0
    elif (r1 + c1 == r2 + c2 or r1 - c1 == r2 - c2):
        b = 1
    else:
        b = 2  
    
    print(r, b, k)

solve()