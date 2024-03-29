def solve():
    a, b, c = map(int, input().split())
    if a<b<c:
        print('STAIR')
    elif a<b>c:
        print('PEAK')
    else:
        print('NONE')

t = int(input())
for _ in range(t):
    solve()