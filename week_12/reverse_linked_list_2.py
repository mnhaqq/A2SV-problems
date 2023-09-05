# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        left_prev = dummy
        ptr = dummy.next
        i = 0
        while i < left - 1 and ptr:
            left_prev = ptr
            ptr = ptr.next
            i+=1
        
        i = 0
        prev = None
        while ptr and i < right - left + 1:
            _next = ptr.next
            ptr.next = prev
            prev = ptr
            ptr = _next
            i+=1

        left_prev.next.next = ptr
        left_prev.next = prev

        return dummy.next