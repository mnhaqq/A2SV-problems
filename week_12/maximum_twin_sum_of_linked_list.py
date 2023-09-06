# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = fast = head
        while fast:
            fast = fast.next
            if fast and fast.next:
                fast = fast.next
                slow = slow.next
        
        prev = slow
        ptr = prev.next
        prev.next = None
        while prev != None and ptr != None:
            _next = ptr.next
            ptr.next = prev
            prev = ptr
            ptr = _next
        head_2 = prev

        maxx = 0
        left = head
        right = head_2
        while left and right:
            maxx = max(maxx, right.val+left.val)
            left = left.next
            right = right.next
        return maxx