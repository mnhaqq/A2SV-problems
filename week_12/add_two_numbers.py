# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_answer = ListNode()
        ptr = dummy_answer
        ptr1 = l1
        ptr2 = l2
        ans = res = carry = 0
        while ptr1 or ptr2:
            ans = 0
            if ptr1:
                ans += ptr1.val
                ptr1 = ptr1.next
            if ptr2:
                ans += ptr2.val
                ptr2 = ptr2.next
            ans += carry
            res = ans % 10
            if ans > 9:
                carry = ans // 10
            else:
                carry = 0
            _new = ListNode(res)
            ptr.next = _new
            ptr = ptr.next
        if carry > 0:
            _new = ListNode(carry)
            ptr.next = _new
            ptr = ptr.next
        return dummy_answer.next
    
        