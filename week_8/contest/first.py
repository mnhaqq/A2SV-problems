from collections import Counter
def solve():
    s=input()
    dic=Counter(s)
    new_string=""
    for key, value in dic.items():
        if value == 2:
            new_string+=key*2
        else:
            new_string+=key
    print(new_string)

t=int(input())
for _ in range(t):
    solve()