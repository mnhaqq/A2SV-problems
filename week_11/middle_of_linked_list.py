# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.slow = self.fast = head
        while self.fast:
            self.fast = self.fast.next
            if self.fast:
                self.fast = self.fast.next
                self.slow = self.slow.next
        return self.slow
