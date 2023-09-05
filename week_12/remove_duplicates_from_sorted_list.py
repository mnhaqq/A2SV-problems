# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dic = dict()
        ptr = head
        while ptr:
            dic[ptr.val] = dic.get(ptr.val, 0) + 1
            ptr = ptr.next

        ptr = head
        prev = dummy
        while ptr:
            if dic.get(ptr.val) == 1:
                prev.next = ptr
                prev = ptr
            ptr = ptr.next
        prev.next = None

        return dummy.next
        