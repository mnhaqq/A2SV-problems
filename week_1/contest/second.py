n = int(input())
a = list(map(int, input().split()))

total = sum(a)
sought = []
for i in range(len(a)):
    arithmetic_mean = (total - a[i])/(len(a)-1)
    if arithmetic_mean == a[i]:
        sought.append(i+1)

sought.sort()
print(len(sought))
print(*sought)