from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode(float("-inf"), head)
        boundary = head
        ptr = head.next

        while ptr:
            if ptr.val >= boundary.val:
                boundary = boundary.next
            else:
                prev = dummy
                while prev.next.val <= ptr.val:
                    prev = prev.next

                boundary.next = ptr.next
                ptr.next = prev.next
                prev.next = ptr
            ptr = boundary.next
        return dummy.next