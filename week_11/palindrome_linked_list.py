# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #find middle index
        slow = fast = head
        while fast:
            fast = fast.next
            if fast and fast.next:
                fast = fast.next
                slow = slow.next
        
        #reverse the second part of the linked list
        prev = slow
        ptr = prev.next
        prev.next = None
        while prev != None and ptr != None:
            _next = ptr.next
            ptr.next = prev
            prev = ptr
            ptr = _next
        head_2 = prev
        
        #check if the first part and reversed second part have the same values
        left = head
        right = head_2
        while left and right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True