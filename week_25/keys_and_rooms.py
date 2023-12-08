from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        visited = set([0])
        queue = deque()
        queue.append(rooms[0])

        while queue:
            keys = queue.popleft()

            for key in keys:
                if key not in visited:
                    visited.add(key)
                    queue.append(rooms[key])
                    
        return len(visited) == len(rooms)
