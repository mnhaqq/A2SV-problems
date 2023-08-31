# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        prev = head
        ptr = prev.next
        head.next = None
        while prev != None and ptr != None:
            _next = ptr.next
            ptr.next = prev
            prev = ptr
            ptr = _next
        head = prev
        return head
            