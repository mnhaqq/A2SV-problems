def solve():
    n = int(input())
    a = list(map(int, input().split()))

    negatives = zeros = 0
    
    coins = 0
    for i in range(n):
        if a[i] < 0:
            negatives += 1
        elif a[i] == 0:
            zeros += 1
        coins += min(abs(a[i]+1), abs(a[i]-1))

    if negatives%2 != 0 and zeros == 0:
        coins += 2
    
    print(coins)

solve()