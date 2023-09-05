# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()

        ptr = head
        new_ptr = dummy
        while ptr:
            slow = ptr
            fast = slow.next
            count = 0
            while fast and slow.val == fast.val:
                count += 1
                fast = fast.next
            if count == 0:
                new_ptr.next = slow
                new_ptr = new_ptr.next
            ptr = fast
        if new_ptr:
            new_ptr.next = None
        return dummy.next
