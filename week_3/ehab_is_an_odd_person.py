def solve():
    n = int(input())
    a = list(map(int, input().split()))

    count_even=count_odd=0
    for i in range(n):
        if a[i]%2==0:
            count_even+=1
        else:
            count_odd+=1
    
    if count_even > 0 and count_odd > 0:
        a.sort()
    print(*a)

if "__main__" == __name__:
    solve()