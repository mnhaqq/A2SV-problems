# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        self.slow = self.fast = head
        while self.slow.next != None:
            self.slow = self.slow.next
            if self.fast:
                self.fast = self.fast.next
            if self.fast:
                self.fast = self.fast.next
            if self.slow == self.fast:
                return True
        return False