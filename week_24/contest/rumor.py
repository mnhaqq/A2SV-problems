import sys
import threading

def main():
   solve()

def solve():
    n, m = map(int, input().split())
    c = list(map(int, input().split()))
    pairs = []
    for _ in range(m):
        pairs.append(list(map(int, input().split())))

    adj_list = dict()
    for i in range(1, n+1):
        adj_list[i] = []
    
    for a, b in pairs:
        adj_list[a].append(b)
        adj_list[b].append(a)
    
    def dfs(node):
        nonlocal tmp
        if colors[node-1] != -1 or not adj_list[node]:
            tmp = min(tmp, c[node-1])
            return tmp
        colors[node-1] = 1
        tmp = c[node-1]
        for neighbour in adj_list[node]:
            tmp = min(tmp, dfs(neighbour))
        return tmp

    ans = 0
    colors = [-1] * n
    if not pairs:
        ans = sum(c)
        print(ans)
        return
    for i in range(len(colors)):
        if colors[i] == -1:
            tmp = float("inf")
            ans += dfs(i+1)
    print(ans)


 
if __name__ == '__main__':
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()