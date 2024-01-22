from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        #find length of list
        i = 0
        ptr = head
        while ptr:
            ptr = ptr.next
            i += 1
        
        #making k be in range of length of list
        k = k % i
        if k == 0:
            return head

        fast = slow = head
        prev = None

        #making distance k between slow and fast
        i = 0
        while fast and i < (k-1):
            fast = fast.next
            i += 1

        #moving pointers to right positions
        while fast.next:
            fast = fast.next
            prev = slow
            slow = slow.next
        
        #rotating list
        if prev:
            prev.next = None
            fast.next = head
            
        return slow