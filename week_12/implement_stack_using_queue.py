class ListNode:
    def __init__(self, value=0, _next=None):
        self.value = value
        self.next = _next

class MyStack:
    def __init__(self):
        self.dummy = ListNode(0, None)

    def push(self, x: int) -> None:
        _new = ListNode(x, self.dummy.next)
        self.dummy.next = _new

    def pop(self) -> int:
        value = self.dummy.next.value
        self.dummy.next = self.dummy.next.next
        return value

    def top(self) -> int:
        return self.dummy.next.value

    def empty(self) -> bool:
        if not self.dummy.next:
            return True
        return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()