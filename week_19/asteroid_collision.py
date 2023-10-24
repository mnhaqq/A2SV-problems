class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        for i in range(len(asteroids)):
            stack.append(asteroids[i])
            
            while len(stack) > 1 and stack[-2] > 0 and stack[-1] < 0:
                a = stack.pop()
                b = stack.pop()
                if abs(a) > abs(b):
                    stack.append(a)
                elif abs(a) < abs(b):
                    stack.append(b)
        return stack