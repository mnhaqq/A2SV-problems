from collections import deque

class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        queue = deque(["0000"])
        visited = set(deadends)
        count = 0
        if "0000" in visited:
            return -1

        visited.add("0000")
        while queue:
            len_level = len(queue)
            for _ in range(len_level):
                node = queue.popleft()
                
                if node == target:
                    return count
                for i in range(len(node)):
                    for j in [-1, 1]:
                        x = int(node[i]) + j
                        if x < 0:
                            x = 9
                        if x > 9:
                            x = 0
                        x = str(x)
                        new = str(node[:i] + x + node[i+1:])
                        if new not in visited:
                            queue.append(new)
                            visited.add(new)
            count += 1

        return -1