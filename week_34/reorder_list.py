from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #put all nodes in list on stack
        stack = []
        ptr = head
        while ptr:
            stack.append(ptr)
            ptr = ptr.next

        num_elems = len(stack)
        if num_elems % 2 == 0:
            num_elems = num_elems // 2
        else:
            num_elems = (num_elems // 2) + 1
        left = head
        while len(stack) > num_elems:
            _next = left.next
            node = stack.pop()
            left.next = node
            left = _next
            node.next = left
        left.next = None