def solve():
    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    
    curr_mouse = len(x)-1
    cat = saved_mice = 0

    while cat < x[curr_mouse]:
        distance = n - x[curr_mouse]
        cat += distance 
        saved_mice += 1
        x[curr_mouse] = 0
        curr_mouse -= 1
    print(saved_mice)

t = int(input())
for _ in range(t):
    solve()