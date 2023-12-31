class MyQueue:
    def __init__(self):
        self.stack_1 = []

    def push(self, x: int) -> None:
        self.stack_1.append(x)

    def pop(self) -> int:
        self.stack_2 = []
        while self.stack_1:
            self.stack_2.append(self.stack_1.pop())
        ans = self.stack_2.pop()
        while self.stack_2:
            self.stack_1.append(self.stack_2.pop())
        return ans

    def peek(self) -> int:
        self.stack_2 = []
        while self.stack_1:
            self.stack_2.append(self.stack_1.pop())
        ans = self.stack_2[-1]
        while self.stack_2:
            self.stack_1.append(self.stack_2.pop())
        return ans

    def empty(self) -> bool:
        if not self.stack_1:
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()