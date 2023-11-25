from collections import defaultdict
import sys

def solve():
    sys.setrecursionlimit(2000)
    n = int(input())
    p = []
    for _ in range(n):
        p.append(int(input()))
    
    adj_list = defaultdict(list)
    for i in range(n):
        if p[i] == -1:
            continue
        adj_list[p[i]].append(i+1)
    
    colors = [-1] * n
    def dfs(num, color):
        if colors[num-1] == -1:
            colors[num-1] = color
        for neighbor in adj_list[num]:
            dfs(neighbor, color+1)

    for i in range(n):
        if p[i] == -1:
            dfs(i+1, 0)
    print(len(set(colors)))


solve()