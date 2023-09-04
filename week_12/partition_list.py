# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        greater_dummy = ListNode(0)
        smaller_dummy = ListNode(0)
        greater_ptr = greater_dummy
        smaller_ptr = smaller_dummy
        ptr = head
        while ptr:
            if ptr.val < x:
                smaller_ptr.next = ptr
                smaller_ptr = smaller_ptr.next
            else:
                greater_ptr.next = ptr
                greater_ptr = greater_ptr.next
            ptr = ptr.next
        if smaller_dummy.next:
            head = smaller_dummy.next
        else:
            head = greater_dummy.next
        smaller_ptr.next = greater_dummy.next
        greater_ptr.next = None
        return head