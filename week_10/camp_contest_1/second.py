n = int(input())
a = list(map(int, input().split()))
m = int(input())
q = list(map(int, input().split()))

a.sort(reverse=True)
total_amt = sum(a)
for i in range(m):
    print(total_amt-a[q[i]-1])