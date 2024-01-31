from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, ptr = dummy, head

        while ptr:
            if ptr.val == val:
                prev.next = ptr.next
            else:
                prev = ptr
            ptr = ptr.next
        return dummy.next