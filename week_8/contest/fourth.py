from collections import Counter
def solve():
    n=int(input())
    a=list(map(int, input().split()))
    perms=0
    count_ppl=0

    if a.count(a[0])==len(a) and a[0] < len(a):
        print(2)
        return
    if sorted(a)==a:
        print(1)
        return
    dic = Counter(a)
    a=list(set(a))
    a.sort()
    for i in range(len(a)):
        count_ppl+=dic.get(a[i])
        if count_ppl > a[i]:
            perms+=1
    print(perms)

t=int(input())
for _ in range(t):
    solve()