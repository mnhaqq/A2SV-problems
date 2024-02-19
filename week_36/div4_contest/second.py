def solve():
    n = int(input())

    arr = []
    for _ in range(n):
        arr.append(input())
    
    count = 0
    for i in range(n):
        if count and arr[i].count('1') == count:
            print('SQUARE')
            return
        elif count:
            print('TRIANGLE')
            return
        count = arr[i].count('1')


t = int(input())
for _ in range(t):
    solve()