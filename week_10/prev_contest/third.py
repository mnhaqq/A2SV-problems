from collections import Counter
def solve():
    n = int(input())
    l = list(map(int, input().split()))

    dic = Counter(l)
    largest = 0
    for key, value in dic.items():
        largest = max(largest, value)
    print(largest, len(dic))

solve()