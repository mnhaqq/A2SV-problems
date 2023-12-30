class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        dest_time = sorted(zip(position, speed))
        
        stack = deque()

        for p, s in dest_time:
            t = (target - p) / s
            while stack and t >= stack[-1]:
                stack.pop()
            stack.append(t)
        return len(stack)