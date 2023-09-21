def solve():
    n, k = map(int, input().split())
    s = input()

    ans =r=0
    while r < n:
        if s[r]=="B":
            ans += 1
            r+=k-1
        r+=1
    print(ans)
        
        




t = int(input())
for _ in range(t):
    solve()