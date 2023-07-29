def solve():
    n=int(input())
    s=input()

    l=0
    r=n-1
    shortest_length=n
    while l<r:
        if s[l]!=s[r]:
            shortest_length-=2
        else:
            break
        l+=1
        r-=1
    print(shortest_length)

t=int(input())
for _ in range(t):
    solve()