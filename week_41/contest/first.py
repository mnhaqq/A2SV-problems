def solve():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))

    ans = sum(a)
    num_even = num_odd = 0
    for i in range(n):
        if a[i] % 2 == 0:
            num_even += 1
        else:
            num_odd += 1

    for _ in range(q):
        q_t, add = map(int, input().split())
        
        if q_t == 0:
            ans += (num_even * add)
            if add % 2 != 0:
                num_even = 0
                num_odd = n
        
        elif q_t == 1:
            ans += (num_odd * add)
            if add % 2 != 0:
                num_odd = 0
                num_even = n
        
        print(ans)


t = int(input())
for _ in range(t):
    solve()