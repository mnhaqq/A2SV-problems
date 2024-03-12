# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        dic = dict()
        pr_sum = 0

        ptr = dummy
        while ptr:
            pr_sum += ptr.val
            dic[pr_sum] = ptr
            ptr = ptr.next

        ptr = dummy
        pr_sum = 0
        while ptr:
            pr_sum += ptr.val
            if pr_sum in dic:
                ptr.next = dic[pr_sum].next
            ptr = ptr.next

        return dummy.next
