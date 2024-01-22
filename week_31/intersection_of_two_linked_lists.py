from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a = set()
        b = set()

        ptr_a = headA
        ptr_b = headB

        while ptr_a or ptr_b:
            if ptr_a:
                a.add(ptr_a)
                if ptr_a in b:
                    return ptr_a
                ptr_a = ptr_a.next
            
            if ptr_b:
                b.add(ptr_b)
                if ptr_b in a:
                    return ptr_b
                ptr_b = ptr_b.next
        return None