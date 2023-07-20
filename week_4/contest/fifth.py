n=int(input())
a=list(map(int, input().split()))

a.sort()
left=right=count=0
while left<n:
    while right < n and a[right]-a[left]<=5:
        right+=1
    count=max(count, right-left)
    left+=1
print(count)