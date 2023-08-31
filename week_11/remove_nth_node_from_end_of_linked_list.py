# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = fast = head
        i = 0
        while i < n and fast:
            fast = fast.next
            i+=1
        if not fast:
            if head:
                head = head.next
            return head
        while fast.next:
            slow = slow.next
            fast = fast.next
        if slow.next:
            slow.next = slow.next.next
        return head
