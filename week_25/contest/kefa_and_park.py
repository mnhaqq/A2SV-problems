import sys
import threading

def main():
   solve()

def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    p = []
    for i in range(n-1):
        p.append(list(map(int, input().split())))

    adj_list = dict()
    for i in range(1, n+1):
        adj_list[i] = []
    for x, y in p:
        adj_list[x].append(y)
        adj_list[y].append(x)


    def dfs(node, consec_cats):
        nonlocal ans
        if consec_cats > m:
            return
        
        if not adj_list[node] or (len(adj_list[node]) == 1 and adj_list[node][0] in visited):
            ans += 1
            return
        
        visited.add(node)
        for nei in adj_list[node]:
            if nei not in visited:
                if a[nei-1] == 1:
                    dfs(nei, consec_cats + 1)
                else:
                    dfs(nei, a[nei-1])

    ans = 0
    visited = set()
    dfs(1, a[0])   
    print(ans) 


if __name__ == '__main__':
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()