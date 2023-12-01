from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = slow = fast = dummy
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next
            if fast: 
                fast = fast.next
        if prev and prev.next:
            prev.next = prev.next.next
        return dummy.next