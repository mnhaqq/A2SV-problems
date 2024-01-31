from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #reverse linked list
        prev = None
        ptr = head

        while ptr:
            _next = ptr.next
            ptr.next = prev
            prev = ptr
            ptr = _next

        #remove nodes
        left = head = prev
        maxx = head.val
        right = left.next

        while right:
            if right.val < left.val:
                right = right.next
            else:
                left.next = right
                left = left.next
                right = right.next
        left.next = None

        #re reverse list
        prev = None
        ptr = head

        while ptr:
            _next = ptr.next
            ptr.next = prev
            prev = ptr
            ptr = _next
        return prev
