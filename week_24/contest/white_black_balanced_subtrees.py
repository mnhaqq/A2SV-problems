from collections import defaultdict
import sys, threading
 
def main():
    def solve():
        def dfs(node):
            nonlocal visited, balanced_trees
            if node in visited:
                return 0
 
            visited.add(node)
            if colors[node-1] == "B":
                curr = 1
            else:
                curr = -1

            res = 0
            for neighbour in neighbours[node]:
                res += dfs(neighbour)
 
            if res + curr == 0:
                balanced_trees += 1
            return res + curr
 
 
        neighbours = defaultdict(list)
 
        n = int(input())
        parents = list(map(int, input().split()))
        colors = [color for color in input()]
 
        for i in range(len(parents)):
            neighbours[parents[i]].append(i+2)
        
        visited = set()
        balanced_trees = 0
        dfs(1)
        print(balanced_trees)
    
    t = int(input())
    for _ in range(t):
        solve()
sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)
 
main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()