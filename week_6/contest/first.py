k,n,w=map(int, input().split())

total_cost=0
for i in range(w):
    total_cost+=k*(i+1)
if total_cost-n >0:
    print(total_cost-n)
else:
    print(0)