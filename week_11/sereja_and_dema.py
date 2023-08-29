n = int(input())
cards = list(map(int, input().split()))

sejeda = dima = i = 0
l, r = 0, n-1
while l <= r:
    if cards[r] >= cards[l]:
        val = cards[r]
        r-=1
    else:
        val = cards[l]
        l+=1
    if i % 2 == 0:
        sejeda+=val
    else:
        dima+=val
    i+=1

if l==r:
    sejeda+=cards[l]
print(sejeda, dima)