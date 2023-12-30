from collections import deque

class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        dest_time = sorted(zip(position, speed))
        
        stack = deque()

        for p, s in dest_time:
            t = (target - p) / s
            while stack and t >= stack[-1]:
                stack.pop()
            stack.append(t)
        return len(stack)