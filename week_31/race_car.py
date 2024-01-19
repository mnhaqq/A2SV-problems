from collections import deque

class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(0, 1)])

        level = 0
        while queue:
            len_level = len(queue)

            for _ in range(len_level):
                pos, spd = queue.popleft()
                if pos == target:
                    return level

                queue.append((pos + spd, spd * 2))
                
                if (pos + spd > target and spd > 0) or (pos + spd < target and spd < 0):
                    if spd > 0:
                        spd = -1
                    else:
                        spd = 1
                    queue.append((pos, spd))
            level += 1
