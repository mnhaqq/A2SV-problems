from collections import deque

class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        def check_exit(a, b):
            return a == 0 or a == len(maze)-1 or b == 0 or b == len(maze[0])-1
        
        def inbound(a, b):
            return 0 <= a < len(maze) and 0 <= b < len(maze[0])

        moves = [(-1,0), (0,-1), (1,0), (0,1)]
        visited = set()
        visited.add(tuple(entrance))
        
        queue = deque()
        queue.append(tuple(entrance))

        ans = 0
        while queue:
            len_level = len(queue)

            for _ in range(len_level):
                r, c = queue.popleft()
                if check_exit(r, c) and (r, c) != tuple(entrance):
                    print(r, c)
                    return ans

                for a, b in moves:
                    if (r+a, c+b) in visited or not inbound(r+a, c+b):
                        continue
                    if maze[r+a][c+b] == "+":
                        continue
                    visited.add((r+a, c+b))
                    queue.append((r+a, c+b))
            ans += 1

        return -1