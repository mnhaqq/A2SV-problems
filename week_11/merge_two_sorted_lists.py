# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        ptr = dummy
        l1_ptr = list1
        l2_ptr = list2
        while l1_ptr and l2_ptr:
            if l1_ptr.val <= l2_ptr.val:
                ptr.next = l1_ptr
                ptr = ptr.next
                l1_ptr = l1_ptr.next
            else:
                ptr.next = l2_ptr
                ptr = ptr.next
                l2_ptr = l2_ptr.next

        ptr.next = l1_ptr or l2_ptr
        if l1_ptr:
            ptr.next = l1_ptr
        elif l2_ptr:
            ptr.next = l2_ptr
 
        return dummy.next
        