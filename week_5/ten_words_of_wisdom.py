def solve():
    n=int(input())
    matrix=[]
    quality=float("-inf")
    for i in range(n):
        matrix.append(list(map(int, input().split())))
        if matrix[i][0]<=10 and matrix[i][1]>quality:
            quality=matrix[i][1]
            ans=i+1
    print(ans)
        

t=int(input())
for _ in range(t):
    solve()