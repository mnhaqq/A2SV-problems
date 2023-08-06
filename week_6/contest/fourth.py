n,d=map(int, input().split())

matrix=[]
for i in range(n):
    a,b=map(int, input().split())
    matrix.append([a,b])

matrix.sort()

maximum=0
tmp=0
l=0
for r in range(n):
    while matrix[r][0]-matrix[l][0]>=d:
        tmp-=matrix[l][1]
        l+=1
    tmp+=matrix[r][1]
    maximum=max(tmp,maximum)
print(maximum)