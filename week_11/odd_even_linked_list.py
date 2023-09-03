# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        odd_head = ptr = head
        even_head = head.next

        while ptr and ptr.next:
           _next = ptr.next
           prev = ptr
           ptr.next  = ptr.next.next
           ptr = ptr.next
           if _next and _next.next:
                _next.next = _next.next.next
        if ptr:
            ptr.next = even_head
        else:
            prev.next = even_head
        return odd_head
        