# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        len_list = 0
        ptr = head
        while ptr:
            len_list += 1
            ptr = ptr.next
        ans = 0
        i = 1
        ptr = head
        while ptr:
            ans += ptr.val * (2**(len_list-i))
            i+=1
            ptr = ptr.next
        return ans
        