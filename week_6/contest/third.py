n=int(input())
a=list(map(int, input().split()))
m=int(input())
b=list(map(int, input().split()))

a.sort()
b.sort()
pairs=0
for i in range(n):
    j=0
    while j<len(b):
        if abs(a[i]-b[j])<=1:
            pairs+=1
            b.pop(j)
            break
        j+=1
print(pairs)