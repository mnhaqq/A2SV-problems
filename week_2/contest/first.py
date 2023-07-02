def solve():
    n = int(input())
    l = list(map(int, input().split()))
    counter = [0] * (max(l)+1)
    for i in range(n):
        counter[l[i]]+=1
    for i in range(1, len(counter)):
        if counter[i-1] < counter[i]:
            print("NO") 
            return
    print("YES")


t = int(input())
for _ in range(t):
    solve()