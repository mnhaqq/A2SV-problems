# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        slow = fast = head
        while slow.next != None:
            slow = slow.next
            if fast:
                fast = fast.next
            if fast:
                fast = fast.next
            if slow == fast:
                return True
        return False