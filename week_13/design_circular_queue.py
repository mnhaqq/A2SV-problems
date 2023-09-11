class Node:
    def __init__(self, val=0, _next=None):
        self.val = val
        self.next = _next

class MyCircularQueue:
    def __init__(self, k: int):
        self.dummy = Node()
        self.tail = self.dummy
        self.counter = 0
        self.k = k

    def enQueue(self, value: int) -> bool:
        if self.counter < self.k:
            self.counter += 1
            _new = Node(value)
            self.tail.next = _new
            self.tail = _new
            return True
        return False

    def deQueue(self) -> bool:
        if self.dummy.next and self.counter > 0:
            self.counter -= 1
            self.dummy.next = self.dummy.next.next   
            if self.counter == 0:
                self.tail = self.dummy
            return True
        return False     

    def Front(self) -> int:
        if self.dummy.next:
            return self.dummy.next.val
        return -1

    def Rear(self) -> int:
        if self.tail != self.dummy:
            return self.tail.val
        return -1

    def isEmpty(self) -> bool:
        if self.counter > 0:
            return False
        return True

    def isFull(self) -> bool:
        if self.counter == self.k:
            return True
        return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()